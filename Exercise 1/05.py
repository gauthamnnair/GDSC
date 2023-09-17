def first_last(l):
	if(l[0]==l[-1]):
		return True
	else:
		return False
lint=list(input("Enter a List of Numbers: "))
print(first_last(lint))
