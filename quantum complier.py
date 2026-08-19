# mini_qcompiler.py
"""
Tiny quantum-compiler demonstration:
- Simple parser for a tiny assembly (H, X, Y, Z, CX)
- Builds an IR: list of Gate(name, targets, controls)
- One optimization pass: cancel consecutive inverse gates (H,H -> I, CX,CX -> I)
- Backend emits a simple OpenQASM-like string
- Statevector simulator to verify equivalence before/after optimization

Run: python mini_qcompiler.py
"""
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np
import math
import sys

# ---------- IR ----------
@dataclass
class Gate:
    name: str
    targets: Tuple[int, ...]
    controls: Tuple[int, ...] = ()

    def __repr__(self):
        if self.controls:
            return f"{self.name} ctrl={self.controls} tgt={self.targets}"
        return f"{self.name} tgt={self.targets}"

# ---------- Parser ----------
def parse_asm(asm: str) -> Tuple[int, List[Gate]]:
    """
    Parse a tiny assembly. Example lines:
      qreg 2
      H q0
      CX q0,q1
      H q0
    Returns: (num_qubits, list_of_gates)
    """
    lines = [ln.strip() for ln in asm.strip().splitlines() if ln.strip() and not ln.strip().startswith("//")]
    if not lines:
        raise ValueError("Empty assembly")
    # first line should be qreg N
    first = lines[0].split()
    if first[0].lower() != "qreg" or len(first) != 2:
        raise ValueError("First line must be: qreg N")
    n_qubits = int(first[1])
    gates: List[Gate] = []
    for ln in lines[1:]:
        parts = ln.replace(",", " ").split()
        op = parts[0].upper()
        args = parts[1:]
        # parse qubit tokens like q0, q1
        def qidx(tok):
            if tok.lower().startswith("q"):
                return int(tok[1:])
            raise ValueError(f"Invalid qubit token: {tok}")
        if op == "CX" or op == "CNOT":
            if len(args) != 2:
                raise ValueError("CX expects 2 args: ctrl target")
            gates.append(Gate("CX", targets=(qidx(args[1]),), controls=(qidx(args[0]),)))
        elif op in ("H","X","Y","Z","S","T"):
            if len(args) != 1:
                raise ValueError(f"{op} expects 1 arg: target")
            gates.append(Gate(op, targets=(qidx(args[0]),)))
        else:
            raise ValueError(f"Unknown op: {op}")
    return n_qubits, gates

# ---------- Optimizer ----------
def optimize_cancel_adjacent(gates: List[Gate]) -> List[Gate]:
    """
    Simple cancellation optimization:
      - H followed by H on same target cancels (H^2 = I)
      - X followed by X cancels, Y Y cancels, Z Z cancels
      - CX followed by CX with same control/target cancels
    This is a single-pass stack-based cancellation.
    """
    stack: List[Gate] = []
    def same_position(g1: Gate, g2: Gate) -> bool:
        return g1.targets == g2.targets and g1.controls == g2.controls and g1.name == g2.name

    for g in gates:
        if stack and same_position(stack[-1], g) and g.name in ("H","X","Y","Z","CX"):
            # cancel the pair
            stack.pop()
        else:
            stack.append(g)
    return stack

# ---------- Backend (emit tiny QASM-like) ----------
def emit_qasm(n_qubits: int, gates: List[Gate]) -> str:
    out = [f"qreg {n_qubits}"]
    for g in gates:
        if g.controls:
            out.append(f"{g.name} q{g.controls[0]},q{g.targets[0]}")
        else:
            out.append(f"{g.name} q{g.targets[0]}")
    return "\n".join(out)

# ---------- Statevector simulator ----------
def kron_many(mats: List[np.ndarray]) -> np.ndarray:
    res = mats[0]
    for m in mats[1:]:
        res = np.kron(res, m)
    return res

def single_qubit_gate_matrix(name: str) -> np.ndarray:
    if name == "H":
        return (1/math.sqrt(2)) * np.array([[1,1],[1,-1]], dtype=complex)
    if name == "X":
        return np.array([[0,1],[1,0]], dtype=complex)
    if name == "Y":
        return np.array([[0,-1j],[1j,0]], dtype=complex)
    if name == "Z":
        return np.array([[1,0],[0,-1]], dtype=complex)
    if name == "S":
        return np.array([[1,0],[0,1j]], dtype=complex)
    if name == "T":
        return np.array([[1,0],[0,math.cos(math.pi/4)+1j*math.sin(math.pi/4)]], dtype=complex)
    raise ValueError(f"Unknown single-qubit gate: {name}")

def cx_matrix(n_qubits: int, control: int, target: int) -> np.ndarray:
    # build 2^n x 2^n matrix for CX by summing projectors
    dim = 1 << n_qubits
    M = np.zeros((dim, dim), dtype=complex)
    for basis in range(dim):
        bit_c = (basis >> control) & 1
        bit_t = (basis >> target) & 1
        if bit_c == 0:
            # unchanged
            M[basis, basis] = 1.0
        else:
            # flip target bit
            flipped = basis ^ (1 << target)
            M[flipped, basis] = 1.0
    return M

def apply_gate(state: np.ndarray, n_qubits: int, gate: Gate) -> np.ndarray:
    dim = 1 << n_qubits
    if gate.name in ("H","X","Y","Z","S","T"):
        # build full operator as tensor of single-qubit ops and identity
        mats = []
        for q in range(n_qubits):
            if q == gate.targets[0]:
                mats.append(single_qubit_gate_matrix(gate.name))
            else:
                mats.append(np.eye(2, dtype=complex))
        U = kron_many(mats[::-1])  # note: ordering q0 as least-significant -> reverse for big-endian
        return U.dot(state)
    elif gate.name == "CX":
        U = cx_matrix(n_qubits, gate.controls[0], gate.targets[0])
        return U.dot(state)
    else:
        raise ValueError(f"Unknown gate in apply: {gate.name}")

def simulate(n_qubits: int, gates: List[Gate]) -> np.ndarray:
    state = np.zeros(1 << n_qubits, dtype=complex)
    state[0] = 1.0  # |00...0>
    for g in gates:
        state = apply_gate(state, n_qubits, g)
    return state

# ---------- Utils ----------
def states_equal_up_to_global_phase(s1: np.ndarray, s2: np.ndarray, tol=1e-8) -> bool:
    # normalize
    if np.linalg.norm(s1) < tol or np.linalg.norm(s2) < tol:
        return np.allclose(s1, s2, atol=tol)
    s1n = s1 / np.linalg.norm(s1)
    s2n = s2 / np.linalg.norm(s2)
    # inner product
    ip = np.vdot(s1n, s2n)
    # |ip| should be ~1 if equal up to global phase
    return abs(abs(ip) - 1.0) < 1e-6

# ---------- Demo / Example ----------
def demo():
    asm = """
    // tiny circuit demonstration
    qreg 2
    H q0
    CX q0,q1
    H q0
    H q0
    CX q0,q1
    X q1
    X q1
    """
    print("=== INPUT ASM ===")
    print(asm)
    n, gates = parse_asm(asm)
    print("Parsed gates:", gates)
    # simulate before optimization
    state_before = simulate(n, gates)
    print("\nStatevector before optimization:\n", np.round(state_before, 6))

    # optimize
    opt = optimize_cancel_adjacent(gates)
    print("\nOptimized gate-list:", opt)
    print("\nEmitted QASM-like backend output:")
    print(emit_qasm(n, opt))

    state_after = simulate(n, opt)
    print("\nStatevector after optimization:\n", np.round(state_after, 6))

    eq = states_equal_up_to_global_phase(state_before, state_after)
    print(f"\nEquivalence check (up to global phase): {eq}")

if __name__ == "__main__":
    demo()
