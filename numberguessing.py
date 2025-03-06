import random
num=random.randint(1,100)
print("Guess a number between 1 and 100:-")
guess=int(input())
if guess==num:
    print("computer guessed:- ",num)
    print("Tie!!!!!\nYour Number is Equal")
elif guess<num:
     print("computer guessed:- ",num)
     print("You Lose!!!!!\nYour Number is Too low")
else:
    print("computer guessed:- ",num)
    print("You Win!!!!!\nYour Number is Too high")