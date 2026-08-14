import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3
symbol_count={
    "A":2,"B":4,"C":6,"D":8
}
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        #_is used for itertive valuse where for unsed variable by (BBB)BY TIM YT CHANEL
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns=[]
    for  _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    #transpose matrix trick let you understand the words and core logic behinf the transpose of the matrix
    for row in range(len(columns[0])):
        for column in columns:
            print(columns[row],"|")
            #unfinised code can complete in future,thank you 





def deposit():
    while True:
        amount=int(input("WHAT WOULD LIKE TO DEPOSIT ? $:"))
        if amount>=0:
            break
        else:
            print("AMOUNT MUST BE GREATER THAN 0")
    return amount
      
    

def get_number_of_lines():
    
    while True:
        lines=int(input("ENTER THE NUMBER OF LINES WOULD YOU LIKE(1-"+str(MAX_LINES)+")?"))
        
        
        if 1<=lines<=MAX_LINES:
            break
        else:
            print(" ENTER NUMBER OF VALID LINES")
        
    return lines
def get_bet():
        while True:
            amount=int(input("WHAT WOULD LIKE TO bet? $:"))
            if MIN_BET<=amount<=MAX_BET:
                break
                
            else:
                print(f"AMOUNT MUST BE BETWEEN,{MIN_BET},AND,{MAX_BET},.")

        return amount
    
    


def main():

    balance=deposit()
    lines=get_number_of_lines()
    while True:

        bet=get_bet()
        total_bet=bet*lines
        if total_bet>=balance:
            print(f"you dont have enough balance for that,your cuurent balance:{balance}")
        else:
            break
        

    
    
    print(f"you are betting {bet} on {lines} lines.total bet is equal to: {total_bet}")

main()

