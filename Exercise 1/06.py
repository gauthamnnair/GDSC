lint=[]
try:
	n=int(input("Enter the Number of Elements of List: "))
	for j in range(n):
		ele=int(input("Enter the Number: "))
		lint.append(ele)
	for i in lint:
		if(i%5==0):
			print(i,end=" ")
except:
	print("Please Enter Valid Number")
