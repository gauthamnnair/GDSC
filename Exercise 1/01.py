def Prod_Sum(m,n):
	if(m*n<=1000):
		return m*n
	else:
		return m+n
a=int(input("Enter the 1st Number: ")) 
b=int(input("Enter the 2nd Number: "))
c=Prod_Sum(a,b)
print("The result is : ",c)
