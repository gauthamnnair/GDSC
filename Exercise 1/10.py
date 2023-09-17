try:
	n=int(input("Enter the Number: "))
	if(n>0):
		while(n>0):
			print(n%10,end=" ")
			n//=10
	else:
		print("Please Enter an Positive Number")
except:
	print("Plese Enter a Number")

