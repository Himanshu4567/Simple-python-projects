import random
l=["rock","paper","scissor"]

while True:
    ccount=0
    ucount=0
    user=int(input("Game Starts...\n1 Yes\n2 No || Exit\n"))
    if user==1:
       for i in range(1,4):
           uinput=int(input("1 Rock\n2 Paper\n3 Scissor\n"))
           if uinput==1:
               uchoice="rock"
           elif uinput==2:
               uchoice="paper"
           elif uinput==3:
               uchoice="scissor"
           cchoice=random.choice(l)
           if uchoice==cchoice:
               print("Computer Choice : ",cchoice)
               print("User Choice : ",uchoice)
               print("Game Draw")
               ucount=ucount+1
               ccount=ccount+1
           elif (uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
               print("Computer Choice : ",cchoice)
               print("User Choice : ",uchoice)
               print("You win !!!")
               ucount=ucount+1
           else :
               print("Computer Choice : ",cchoice)
               print("User Choice : ",uchoice)
               print("Computer win !!!")
               ccount=ccount+1
       if ucount==ccount: 
           print("Final Game Draw")
           print("User count :",ucount)
           print("Computer count :",ccount)
       elif ucount>ccount:
           print("You Win The Final Game !!!")
           print("User count :",ucount)
           print("Computer count :",ccount)
       else:
           print("Computer Win The Final Game !!!")
           print("User count :",ucount)
           print("Computer count :",ccount)    
            
       
    else:
        print("Game Over")
        break
    