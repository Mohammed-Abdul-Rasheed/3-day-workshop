n=int(input())
for row in range(3):
    for column in range(1,n+1):
        if (row+column)%4==0 or row==1 and column%4==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
