list1,list2,list3=[],[],[]
try:	
	n1=int(input("Enter the Numbers of Elements of First List: "))
	print("Enter",n1,"Elements: ")
	for i in range(n1):
		ele=int(input("Enter the Element: "))
		list1.append(ele)
	n2=int(input("\nEnter the Numbers of Elements of Second List: "))
	print("Enter",n2,"Elements: ")
	for i in range(n2):
		ele=int(input("Enter the Element: "))
		list2.append(ele)
	for i in list1:
		if(i%2==1):
			list3.append(i)
	for i in list2:
		if(i%2==0):
			list3.append(i)
	print("\nThe Elements of Final List: ")
	for i in list3:
		print(i,end=" ")
except:
	print("Please Enter a Valid Number")
