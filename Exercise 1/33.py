contact={}
def add():
    name=input("Enter Name: ").title()
    n=int(input("Enter the Phone Number: "))
    em=input("Enter the Email ID: ")
    contact[name]=n,em
    print("Contact Added")
def delete():
    name=input("Enter the Name of Contact to be Deleted: ").title()
    if isin(name):
        del contact[name]
        print("Contact Deleted")
def update():
    name=input("Enter the Name of Contact to be Updated: ").title()
    if isin(name):
        n,em=contact[name]
        while True:
            print("What do you Want to Change: ")
            print("1: Number")
            print("2: EMail")
            print("3: Both")
            ch=int(input("Enter the Choice: "))
            if ch==1:
                n=int(input("Enter the Phone Number: "))
                break
            elif ch==2:
                em=input("Enter the Email ID: ")
                break
            elif ch==3:
                n=int(input("Enter the Phone Number: "))
                em=input("Enter the Email ID: ")
                break
            else:
                print("Enter Valid Choice")
        contact[name]=n,em
        print("Contact Updated")
def getD():
    name=input("Enter the Name of Contact to be Accessed: ").title()
    if isin(name):
        n,em=contact[name]
        print(f"Phone Number: {n}")
        print(f"Email ID: {em}")
def isin(name):
    if name in contact:
        return True
    else:
        print(f"The Contact Name: {name} is not present in Contacts")
ch=0
while ch!=5:
    print("\nMenu")
    print("1: Add Contact")
    print("2: Delete Contact")
    print("3: To Update Information")
    print("4: To Get Data")
    print("5: Exit")
    try:
        ch=int(input("Enter the Choice: "))
        if ch==1:
            add()
        elif ch==2:
            delete()
        elif ch==3:
            update()
        elif ch==4:
            getD()
        elif ch==5:
            break
        else:
            print("Please Enter a Correct Choice")
    except:
        print("Please Enter a Valid Choice")
print("Bye")
