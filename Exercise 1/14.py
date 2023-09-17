try:
	n=int(input("Enter the Number: "))
	f=1
	if(n>-1):
		for i in range(1,n+1):
			f*=i
		print("The Factorial of",n,"is:",f)
	else:
		print("Please Enter an Non Negative Number")
except:
	print("Please Enter a Valid Number")
