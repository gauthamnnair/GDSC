n=int(input("Enter the Number of terms: "))
a,b,t=0,1,1
if(n>2):
	print(a,b,end=" ")
	for i in range(2,n):
		t=a+b
		print(t,end=" ")
		a,b=b,t
elif(n==1):
	print(a)
elif(n==2):
	print(a,b)
else:
	print("Please Enter a Positive Number") 
