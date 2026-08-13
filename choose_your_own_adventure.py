name=input("TYPE YOUR NAME:")
print("WELCOME",name,"TO THIS ADVENTURE")
answer=input("YOU ARE ON DIRTY ROAD,IT HAS COME TO END  AND YOU CAN GO LEFT OR RIGHT .WHICH WAY WOULD LIKE TO GO....?:").lower()
if answer=="left":
    answer=input("YOU COME TO A RIVER,YOU CAN WALK AROUND OR SWIM ACROSS.?TYPE WALK AROUND OR SWIM ACROSS:").lower()
    if answer=="swim":
        print("YOUR ARE EATEN BY AN ALLIGATOR")
    elif answer=="walk":
        print("YOU WALKED FOR MANY Kilometer SORRY YOU ARE DEAD:.......")
    else:
        print("NOT A VALID OPTION ,YOU LOSE.")
elif answer=="right":
    answer=input("YOU COME TO BRIDGE,IT LOOKS WOBBLY,DO YOU WANT CROSS IT OR HEAD BACK TO?(CROSS/BACK):").lower()
    if answer=="back":
        print("YOU GO  BACK AND YOU LOSE")
    elif answer=="cross":
        answer=input("YOU CAN CROSS THE BRIDGE AND DO YOU WANT TO TALK TO THE STRANGER(YES/NO)?:").lower()
        if answer=="yes":
            print("YOU TALKED TO THE STRANGER AND THEY GIVE YOU GOLD .YOU WIN!")

        elif answer=="no":
            print("YOU IGNORED THE STRANGER AND .YOU LOSE")
        else:
            print("YOU CHOOSE A INVALID OPTION GO BACK")



    else:
        print("NOT A VALID OPTION ,YOU LOSE.")


else:
    print("NOT A VALID OPTION .YOU LOSE.........")


print("THANKS FOR PLAYING THIS GAME AND HOPE YOU ENJOYED MY GAME .!!",name)