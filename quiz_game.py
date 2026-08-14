print("welcome to my computer quiz!")

playing=input("do you want play?: ")
if playing.lower() !="yes":
    print("do some shit work out of here.....")
    quit()
print("okay!lets play :)") 
score=0
answer=input("what does cpu stand for?: ")
if answer.lower() =="central processing unit":
    print("your answer was correct.congrats")
    score+=1
else:
    print("incorrect! check again please...")
answer=input("what does  GPU stand for?: ")
if answer.lower() =="graphics processing unit":
    print("your answer was correct.congrats")
    score+=1
else:
    print("incorrect! check again please...")
answer=input("what does RAM stand for?: ")
if answer.lower() =="random access memory":
    print("your answer was correct.congrats")
    score+=1
else:
    print("incorrect! check again please...")
answer=input("what does psu stand for?: ")
if answer.lower() =="power supply":
    print("your answer was correct.congrats")
    score+=1
else:
    print("incorrect! check again please...")
      
print("you got "+ str(score) +" questions correct....wow great job")
the_percentage=score/4*100
if the_percentage>=75:
    print(F"well you made of this quiz {the_percentage}")
else:
    print("you need to have some idea of computers....")

print("GAME OVER DEAR.....")