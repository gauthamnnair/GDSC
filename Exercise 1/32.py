try:
	n=int(input("Enter the Number of Elements of List: "))
	list1=[]
	list_unique=[]
	print("Enter",n,"Elements: ")
	for i in range(0,n):
		ele=int(input("Enter the element: "))
		list1.append(ele)
	for i in list1:
		if i not in list_unique:
			list_unique.append(i)
	print("The Unique Elements are: ",end="")
	for i in list_unique:
		print(i,end=" ")
except:
	print("Please Enter Valid Number")
