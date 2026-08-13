import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll

    


value=roll()
print(value)

while True:
    players=input("ENTER NUMBER OF PLAYERS(1-4):")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("MUST BE BETWEEN 2 AND 4 PLEASE TRY AGAIN")
    else:
        print("INVALID INPUT PLEASE TRY AGAIN AFTER SOMETIME ")
print(players)


max_score=50
players_score=[0 for i in range(players)]
print(players_score)
while max(players_score)<max_score:
    for players_index in range (players):
        print("\nPLAYER",players_index +1,"TURN HAS JUST STARTED!\n")
        current_score+=0
        while True:
            should_roll=input("WOULD LIKE TO ROLL(y)?").lower()
            if should_roll!="yes":
                break
            value=roll()
            if value==1:
                print("YOU ROLLED A 1! TURN DONE")
                current_score=0
                break
            else:
                current_score+=value
                print("YOU ROLLED A",value)
            print("YOUR CURRENT SCORE IS",current_score)

        players_score[players_index]+=current_score
        print("YOUR PLAYERS SCORES IS: ",players_score[players_index])
print(players_score)














