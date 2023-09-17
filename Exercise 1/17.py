os=input("Enter the string: ")
s=os.lower()
if(s==s[::-1]):
	print(os,"is Pallindrome String")
else:
	print(os,"is Not a Pallindrome String")
