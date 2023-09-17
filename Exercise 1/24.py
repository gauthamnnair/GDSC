import random as r
def PasswordGenerator(length):
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    special="!@#$%^&*()_+{}[]|:;<>,.?/~"
    num="0123456789"
    all_char=upper+lower+special+num
    password=r.choice(upper)+r.choice(lower)+r.choice(special)+r.choice(num)
    for i in range(length-4):
        password+=r.choice(all_char)
    plist=list(password)
    password=""
    r.shuffle(plist)
    password="".join(plist)
    return password
try:
    n=int(input("Enter the Number of Characters[8 or above]: "))
    if(n<8):
        print("Please Enter Larger Number")
    else:
        print("The Password of",n,"Characters: ",PasswordGenerator(n))
except:
    print("Please Enter Valid Number")
