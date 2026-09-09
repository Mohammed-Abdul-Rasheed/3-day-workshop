n=int(input())
for i in range(n):
    if i==0:
        print("*"*(2*n-1))
    else:
        print("*"*(n-i)+" "*(2*i-1)+"*"*(n-i))
for i in range(n-2,-1,-1):
    if i==0:
        print("*"*(2*n-1))
    else:
        print("*"*(n-i)+" "*(2*i-1)+"*"*(n-i))
