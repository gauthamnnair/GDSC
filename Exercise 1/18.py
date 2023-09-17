from random import choice as ch
user=input("Enter Your Choice: ").title()
if (user=="Rock" or user=="Scissors" or user=="Paper"):
    comp=ch(["Rock","Paper","Scissors"])
    if(user==comp):
            print("User:",user,"Computer:",comp)
            print("Its a tie!!")
    elif((user=="Rock"and comp=="Scissors")or(user=="Paper"and comp=="Rock")or(user=="Scissors"and comp=="Paper")):
        print("User:",user,"beats Computer:",comp)
        print("You Won!!")
    else:
        print("Computer:",comp,"beats User:",user)
        print("You Lost!!")
else:
        print("Please Enter Valid Choices [Rock/Paper/Scissors]")
