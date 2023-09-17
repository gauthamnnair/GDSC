try:
    print("Enter a Total of 10 Numbers: ")
    pre=int(input("Enter the First Number: "))
    for i in range(9):
        cur=int(input("Enter the Next Number: "))
        print("The Sum of Previous and Current Numbers:",pre+cur)
        pre=cur
except:
        print("Please Enter Valid Numbers")
