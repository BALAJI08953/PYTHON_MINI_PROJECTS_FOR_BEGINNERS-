import random
OPERATORS=["+","-","*"]
MIN_OPERAND=3
MAX_OPERAND=12

def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operators=random.choice(OPERATORS)

    expr=str(left)+" "+operators+"  "+str(right)
    print(expr)
    answer=eval(expr)
    return expr,answer

expr,answer=generate_problem()
print(expr,answer)