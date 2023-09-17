import random
def display(b):
    for r in b:
       print(" | ".join(r))
       print('-'*10)
def check_win(b,player):
    for r in b:
        if all(cell==player for cell in r):
            return True
    for c in range(3):
        if all(b[r][c]==player for r in range(3)):
           return True
    if all(b[i][i]==player or b[i][2-i]==player for i in range(3)):
        return True
    return False

def comp_move(b):
    for r in range(3):
        for c in range(3):
            if b[r][c]==' ':
                b[r][c]='O'
                if check_win(b,'O'):
                    return
                b[r][c]=' '
    for r in range(3):
        for c in range(3):
            if b[r][c]==' ':
                b[r][c]='X'
                if check_win(b,'X'):
                    b[r][c]='O'
                    return
                b[r][c]=' '
    if b[1][1]==' ':
        b[1][1]='O'
        return
    corl=[(0,0),(0,2),(2,0),(2,2)]
    random.shuffle(corl)
    for r,c in corl:
        if b[r][c]==' ':
            b[r][c]='O'
            return
    sidel=[(0,1),(1,0),(1,2),(2,1)]
    random.shuffle(sidel)
    for r,c in sidel:
        if b[r][c]==' ':
            b[r][c]='O'
            return
def full(b):
    if all(cell!=' ' for r in b for cell in r):
        return True
board=[[' ' for i in range(3)] for i in range(3)]
display(board)
print("Start the Game:")
while True:
    while True:
        try:
            r=int(input("Enter the Row Number[0,1,2]: "))
            c=int(input("Enter the Colum Number[0,1,2]: "))
            if -1<r<3 and -1<c<3 and board[r][c]==' ':
                board[r][c]='X'
                break
            else:
                print("Invalid Move Please Enter Some Other Position")
        except:
            print("Please Enter a Valid Number")
    print("Your Move:")
    display(board)
    if check_win(board,'X'):
        print("You Won!!")
        break
    elif full(board):
        print("Its a Tie!!")
        break
    else:
        comp_move(board)
        print("Computer's Move:")
        display(board)
        if check_win(board,'O'):
            print("Computer Won!!")
            break


                
