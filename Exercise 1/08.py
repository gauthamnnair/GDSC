n=int(input("Enter the Number: "))
ncopy=n
pn=0
while(n>0):
	d=n%10
	n//=10
	pn=pn*10+d
if(pn==ncopy):
	print(ncopy,"is a Pallindrome Number")
else:
	print(ncopy,"is NOT a Pallindrome Number")
