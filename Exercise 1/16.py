n=int(input("Enter the Number: "))
c=0
if(n>1):
	for i in range(2,n):
		if(n%i==0):
			c+=1
	if(c==0):
		print(n,"is a Prime Number")
	else:
		print(n,"is Not a Prime Number")
else:
	print(n,"is Not a Prime Number")

