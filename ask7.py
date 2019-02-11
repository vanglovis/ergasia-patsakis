board = [" "]*9
temp=0
while temp==0:
    temp1=1
    while temp1==1:
        print(board[0:3])
        print(board[3:6])
        print(board[6:10])
        x=input("Type an interval from [1,1] to [3,3]: ")
        if x[1:2]=="1":
            if   x[3:4]=="1":
                if board[0]==" ":
                    board[0]='X'   
                    temp1=2 
                else:
                    print ("Choose another position from [1,1] to 3,3]: ")             
            elif x[3:4]=="2":
                if board[1]==" ":
                    board[1]="X"
                    temp1=2
                else:
                    print ("Choose another position from [1,1] to [3,3]: ")                
            elif x[3:4]=="3":
                if board[2]==" ":
                    board[2]="X"
                    temp1=2
                else:
                    print ("Choose another position from [1,1] to [3,3]: ")            
        if x[1:2]=="2":
            if   x[3:4]=="1":
                if board[3]==" ":
                    board[3]="X"
                    temp1=2
                else:
                    print ("Choose another position from [1,1] to [3,3]: ")                
            elif x[3:4]=="2":
                if board[4]==" ":
                     board[4]="X"
                     temp1=2 
                else:
                    print ("Choose another position from [1,1] to [3,3]: ")
            elif x[3:4]=="3":
               if board[5]==" ":
                   board[5]="X"
                   temp1=2
               else:
                   print ("Choose another position from [1,1] to [3,3]: ")
        if x[1:2]=="3":
           if   x[3:4]=="1":
               if board[6]==" ":     
                   board[6]="X"
                   temp1=2
               else:
                   print ("Choose another position from [1,1] to [3,3]: ")
                   x = random.randint(0,8)                
           elif x[3:4]=="2":
               if board[7]==" ":
                   board[7]="X"
                   temp1=2 
           elif x[3:4]=="3":
               if board[8]==" ":
                   board[8]="X"
                   temp1=2
    if board[0]=="X":
        if board[1]=="X":
            if board[2]=="X":
                temp=1
                print("You won")
        if board[3]=="X":
            if board[6]=="X":
                temp=1
                print("You won")
        if board[4]=="X":
            if board[8]=="X":
                temp=1
                print("You won")
    if board[1]=="X":
        if board[4]=="X":
            if board[7]=="X":
                temp=1
                print("You won")
    if board[2]=="X":
        if board[4]=="X":
            if board[6]=="X":
                temp=1
                print("You won")
        if board[5]=="X":
            if board[8]=="X":
                temp=1
                print("You won")
    if board[3]=="X":
        if board[4]=="X":
            if board[5]=="X":
                temp=1
                print("You won")
    if board[6]=="X":
        if board[7]=="X":
            if board[8]=="X":
                temp=1
                print("You won")
    temp3=1
    j=0
    for i in range(0,9):
        if board[i]=="X":
            j=j+1
        elif board[i]=="O": 
            j=j+1
    if j==9 :
        if temp==0:
            print ("No one won")
            temp=1
    if j<9:
        if temp==0:
            while temp3==1:   
                import random
                x = random.randint(0,8)
                if board[x]==" ":
                   board[x]="O"
                   temp3=3
        else:
            x=random.randint(0,8)
    if board[0]=="O":
        if board[1]=="O":
            if board[2]=="O":
                temp=1
                print("You lost")
        if board[3]=="O":
            if board[6]=="O":
                temp=1
                print("You lost")
        if board[4]=="O":
            if board[8]=="O":
                temp=1
                print("You lost")
    if board[1]=="O":
        if board[4]=="O":
            if board[7]=="O":
                temp=1
                print("You lost")
    if board[2]=="O":
        if board[4]=="O":
            if board[6]=="O":
                temp=1
                print("You lost")
        if board[5]=="O":
            if board[8]=="O":
                temp=1
                print("You lost")
    if board[3]=="O":
        if board[4]=="O":
            if board[5]=="O":
                temp=1
                print("You lost")
    if board[6]=="O":
        if board[7]=="O":
            if board[8]=="O":
                temp=1
                print("You lost")
print(board[0:3])
print(board[3:6])
print(board[6:10])
