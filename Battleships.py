import sys
p1=[['`','1','2','3','4','5','6','7','8','9','10'],[1,'x','x','x','x','x','x','x','x','x','x'],[2,'x','x','x','x','x','x','I','.','.','.'],
[3,'.','.','.','.','.','.','.','.','.','.'],[4,'.','.','.','.','.','.','.','.','.','.'],[5,'.','.','.','.','.','.','.','.','.','.'],[6,'.','.','.','.','.','.','.','.','.','.'],
[7,'.','.','.','.','.','.','.','.','.','.'],[8,'.','.','.','.','.','.','.','.','.','.'],[9,'.','.','.','.','.','.','.','.','.','.'],[10,'.','.','.','.','.','.','.','.','.','.']]
p2=[['`','1','2','3','4','5','6','7','8','9','10'],[1,'x','x','x','x','x','x','x','x','x','x'],[2,'x','x','x','x','x','x','I','.','.','.'],
[3,'.','.','.','.','.','.','.','.','.','.'],[4,'.','.','.','.','.','.','.','.','.','.'],[5,'.','.','.','.','.','.','.','.','.','.'],[6,'.','.','.','.','.','.','.','.','.','.'],
[7,'.','.','.','.','.','.','.','.','.','.'],[8,'.','.','.','.','.','.','.','.','.','.'],[9,'.','.','.','.','.','.','.','.','.','.'],[10,'.','.','.','.','.','.','.','.','.','.']]
# p1=[['`','1','2','3','4','5','6','7','8','9','10'],[1,'.','.','.','.','.','.','.','.','.','.'],[2,'.','.','.','.','.','.','.','.','.','.'],
# [3,'.','.','.','.','.','.','.','.','.','.'],[4,'.','.','.','.','.','.','.','.','.','.'],[5,'.','.','.','.','.','.','.','.','.','.'],[6,'.','.','.','.','.','.','.','.','.','.'],
# [7,'.','.','.','.','.','.','.','.','.','.'],[8,'.','.','.','.','.','.','.','.','.','.'],[9,'.','.','.','.','.','.','.','.','.','.'],[10,'.','.','.','.','.','.','.','.','.','.']]
# p2=[['`','1','2','3','4','5','6','7','8','9','10'],[1,'.','.','.','.','.','.','.','.','.','.'],[2,'.','.','.','.','.','.','.','.','.','.'],
# [3,'.','.','.','.','.','.','.','.','.','.'],[4,'.','.','.','.','.','.','.','.','.','.'],[5,'.','.','.','.','.','.','.','.','.','.'],[6,'.','.','.','.','.','.','.','.','.','.'],
# [7,'.','.','.','.','.','.','.','.','.','.'],[8,'.','.','.','.','.','.','.','.','.','.'],[9,'.','.','.','.','.','.','.','.','.','.'],[10,'.','.','.','.','.','.','.','.','.','.']]
p1shots=[['`','1','2','3','4','5','6','7','8','9','10'],[1,'.','.','.','.','.','.','.','.','.','.'],[2,'.','.','.','.','.','.','.','.','.','.'],
[3,'.','.','.','.','.','.','.','.','.','.'],[4,'.','.','.','.','.','.','.','.','.','.'],[5,'.','.','.','.','.','.','.','.','.','.'],[6,'.','.','.','.','.','.','.','.','.','.'],
[7,'.','.','.','.','.','.','.','.','.','.'],[8,'.','.','.','.','.','.','.','.','.','.'],[9,'.','.','.','.','.','.','.','.','.','.'],[10,'.','.','.','.','.','.','.','.','.','.']]
p2shots=[['`','1','2','3','4','5','6','7','8','9','10'],[1,'.','.','.','.','.','.','.','.','.','.'],[2,'.','.','.','.','.','.','.','.','.','.'],
[3,'.','.','.','.','.','.','.','.','.','.'],[4,'.','.','.','.','.','.','.','.','.','.'],[5,'.','.','.','.','.','.','.','.','.','.'],[6,'.','.','.','.','.','.','.','.','.','.'],
[7,'.','.','.','.','.','.','.','.','.','.'],[8,'.','.','.','.','.','.','.','.','.','.'],[9,'.','.','.','.','.','.','.','.','.','.'],[10,'.','.','.','.','.','.','.','.','.','.']]
def placeships(board,player):
    horv=input(player+", Enter 'H' or 'V' for horizontal or vertical orientation for length 2 ship:")  
    if horv=='H':    #2 
        row=int(input("Enter starting row: "))
        ran=eval(input("Enter the position in row in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=1:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[row][i]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[row][i]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    elif horv=='V':
        col=int(input("Enter starting column:"))
        ran=eval(input("Enter the position in column in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=1:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[i][col]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[i][col]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    else:
        print("Invalid option!")
        sys.exit()
    horv=input(player+", Enter 'H' or 'V' for horizontal or vertical orientation for 1st length 3 ship:")
    if horv=='H': #3.1
        row=int(input("Enter starting row: "))
        ran=eval(input("Enter the position in row in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=2:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[row][i]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[row][i]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    elif horv=='V':
        col=int(input("Enter starting column:"))
        ran=eval(input("Enter the position in column in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=2:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[i][col]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[i][col]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    else:
        print("Invalid option!")
        sys.exit()
    horv=input(player+", Enter 'H' or 'V' for horizontal or vertical orientation for 2nd length 3 ship:")
    if horv=='H': #3.2
        row=int(input("Enter starting row: "))
        ran=eval(input("Enter the position in row in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=2:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[row][i]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[row][i]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    elif horv=='V':
        col=int(input("Enter starting column:"))
        ran=eval(input("Enter the position in column in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=2:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[i][col]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[i][col]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    else:
        print("Invalid option!")
        sys.exit()
    horv=input(player+", Enter 'H' or 'V' for horizontal or vertical orientation for length 4 ship:")
    if horv=='H': #4
        row=int(input("Enter starting row: "))
        ran=eval(input("Enter the position in row in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=3:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[row][i]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[row][i]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    elif horv=='V':
        col=int(input("Enter starting column:"))
        ran=eval(input("Enter the position in column in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=3:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[i][col]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[i][col]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    else:
        print("Invalid option!")
        sys.exit()
    horv=input(player+", Enter 'H' or 'V' for horizontal or vertical orientation for length 5 ship:")
    if horv=='H': #5
        row=int(input("Enter starting row: "))
        ran=eval(input("Enter the position in row in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=4:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[row][i]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[row][i]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    elif horv=='V':
        col=int(input("Enter starting column:"))
        ran=eval(input("Enter the position in column in the format [start,end]:"))
        if int(ran[1])-int(ran[0])!=4:
            print("Incorrect coordinates!")
            sys.exit()
        else:
            try:
                for i in range(int(ran[0]),int(ran[1])+1):
                    if board[i][col]=='I':
                        print("Already occupied!")
                        sys.exit()
                    else:
                        board[i][col]='I'
            except:
                print("Incorrect coordinates!")
                sys.exit()
    else:
        print("Invalid option!")
        sys.exit()
    return board
def shoot(board,player):
    global p1shots,p2shots,p1,p2
    coords=eval(input(player+", Enter the coordinates for the shot in the format [row,column]"))
    if board[int(coords[0])][int(coords[1])]=='.':
        print("Miss!")
        if player=='Player1':
            p1shots[int(coords[0])][int(coords[1])]='m'
            for i in p1shots:
                print(i)
        else:
            p2shots[int(coords[0])][int(coords[1])]='m'
            for i in p2shots:
                print(i)
    elif board[int(coords[0])][int(coords[1])]=='I':
        print("Hit!")
        if player=='Player1':
            p1shots[int(coords[0])][int(coords[1])]='x'
            p2[int(coords[0])][int(coords[1])]='x'
            for i in p1shots:
                print(i)
            checkover(p2,player)
        else:
            p2shots[int(coords[0])][int(coords[1])]='x'
            p1[int(coords[0])][int(coords[1])]='x'
            for i in p2shots:
                print(i)
            checkover(p1,player)
    else:
        print("Invalid coords!")
        sys.exit()
def checkover(board,winplayer):
    count=0
    for i in range(1,11):
        for j in range(1,11):
            if board[i][j]=='x':
                count+=1
    if count==17:
        print("Game Over! "+winplayer+' has won')
        sys.exit()
# p1=placeships(p1,'Player1')
# p2=placeships(p2,'Player2')
while True:
    shoot(p2,'Player1')
    shoot(p1,'Player2')





            

        





