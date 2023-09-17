from random import randint as r
num=r(1,100)
try:
	user_num=int(input("Guess a Number Between 0 to 101: "))
	while(num!=user_num):
		if(user_num<num):
			print("The Guess is Lower")
		else:
			print("The Guess is Higher")
		user_num=int(input("Enter a Number Again:"))
	print("Your Guess is Correct the Number is: ",num)
except:
	print("Please Enter a Valid Number")
