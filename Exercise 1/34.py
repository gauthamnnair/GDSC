try:
	n=int(input("Enter the Number of Elements in List: "))
	list1=[]
	print("Enter",n,"Elements: ")
	for i in range(n):
		ele=int(input("Enter the Element: "))
		list1.append(ele)
	for i in range(n-1):
		for j in range(n-i-1):
			if 	list1[j]>list1[j+1]:
				list1[j],list1[j+1]=list1[j+1],list1[j]
	print("The Sorted Array:")
	for i in list1:
		print(i,end=" ")
except:
	print("Please Enter the Valid Number")
