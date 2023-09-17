from random import choice as ch
def dis():
    display=""
    for i in comp_word:
        if i in gl:
            display+=i
        else:
            display+="_ "
    return display
comp_word=ch(["apple", "banana", "cherry", "pineapple", "strawberry","cat", "dog", "elephant", "giraffe", "kangaroo", "butterfly", "rainbow", "mountain", "ocean", "astronaut"])
n=len(comp_word)
print(f"You have {n} Number fo Guesses to Guess a {n} Lettered Word")
gl=[]
print(dis())
while n>0:
    c=input("Enter Your Guess: ").lower()
    if len(c)!=1 or not c.isalpha():
        print("Please Enter a Single or Valid Character")
    elif c in gl:
        print("You already Guessed that Word")
    elif c in comp_word:
        print("Good Guess")
        gl.append(c)
        dis()
    else:
        print("Worng Guess")
        n-=1
        gl.append(c)
    print(f"Current State: {dis()}")
    if(comp_word==dis()):
        print("You Won")
        break
    print(f"You have {n} Guess Left")
else:
    print("You Lost")
    print(f"The Word Was {comp_word}")
print("End of Game")
