import random

c_val = ['Rock','Scissor','Paper']

while True:
    Ccount=0
    ucount=0
    uc = int(input('''
    Game Start.....
    1 Start | Yes
    2 Exit | No
    '''))
    if uc == 1:
        for a in range(1,6):
            User_input=int(input(''' 
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if User_input == 1:
                uchoice = "Rock"
            elif User_input == 2:
                uchoice = "Scissor"
            elif User_input == 3:
                uchoice = "Paper"
            else:
                print("You entered the wrong value")
            Cchoice = random.choice(c_val)
            print("your choice is:--", uchoice)
            print("Computer choice is:--",Cchoice)
            if Cchoice == uchoice:
                print("Round is Draw")
                ucount = ucount+1
                Ccount = Ccount+1
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and  Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
                print("You win")
                ucount=ucount+1
            else:
                print("Computer win")
                Ccount=Ccount+1
        print("Your total wins:",ucount)
        print("Computer total wins:", Ccount)
        if ucount == Ccount:
            print("Game is draw")
        elif ucount>Ccount:
            print("You win the Game")
        else:
            print("Computer win the Game")
    else:
        break
