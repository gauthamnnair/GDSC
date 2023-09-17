def remove_chars(s,n):
		return s[n::]
st=input("Enter the String: ")
num=int(input("Enter the Number of Characters to be Removed: "))
if(num<len(st)):
	us=remove_chars(st,num)
	print("The Updated String is: ",us)
else:
	print("Error!! Number of Characters to be Removed Should be Less Than Number of Charcters in String")
