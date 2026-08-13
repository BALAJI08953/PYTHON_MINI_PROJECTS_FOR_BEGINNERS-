import random
user_wins=0
computer_wins=0
options= ["rock","paper","scissors"]

while True:
    user_input=input("TYPE ROCK/PAPER/SCISSORS AND Q TO QUIT THE GAME:").lower()
    if user_input=="q":
        break
    if user_input not in ["rock","paper","scissors"]:
        print("PLEASE ENTER THE NORMAL CHOICE NOT YOUR BULL SHIT")
        continue
    random_pick=random.randint(0,2)
    computer_pick=options[random_pick]
    print("computer picked",computer_pick+".")

    if user_input=="rock" and computer_pick=="scissors":
        print("YOU WON!")
        user_wins+=1
        continue
    elif user_input=="paper" and computer_pick=="rock":
        print("YOU WON DEAR:")
        user_wins+=1
        continue
    elif user_input=="scissors" and computer_pick=="paper":
        print("you won dear")
        user_wins+=1
        continue
    else:
        print("YOU LOST")
        computer_wins+=1
    



print("you won ",user_wins,"times")
print("computer wins",computer_wins,"times")
print("GOOD BYE !")

