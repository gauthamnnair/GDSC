def inputM(row,col):
    mat=[]
    for r in range(row):
        rl=[]
        for c in range(col):
            ele=float(input(f"Enter the Element of Index({r+1},{c+1}): "))
            rl.append(ele)
        mat.append(rl)
    return mat
try:
    r1=int(input("Enter the Number of Rows of 1st Matrix: "))
    c1=int(input("Enter the Number of Column of 1st Matrix: "))
    r2=int(input("Enter the Number of Rows of 2nd Matrix: "))
    c2=int(input("Enter the Number of Column of 2nd Matrix: "))
    if(c1==r2):
        print("Enter Elements of First Matrix:")
        mat1=inputM(r1,c1)
        print("Matrix 1:")
        for r in mat1:
            for c in r:
                print(c,end=" ")
            print() 
        print("Enter Elements of Second Matrix:")
        mat2=inputM(r2,c2)
        print("Matrix 2:")
        for r in mat2:
            for c in r:
                print(c,end=" ")
            print() 
        rmat=[[0 for i in range(c2)]for i in range(r1)]
        for r in range(r1):
            for c in range(c2):            
                for e in range(c1):
                    rmat[r][c]+=mat1[r][e]*mat2[e][c]
        print("The Resultant Mattix is:")
        for r in rmat:
            for c in r:
                print(c,end=" ")
            print() 
    else:
         print("Matrix Multiplication for these 2 Matrix Values are NOT Possible")
except:
    print("Please Enter a Valid Number")
