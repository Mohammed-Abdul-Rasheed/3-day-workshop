n=int(input())
total=0
temp=n
while temp>0:
    digit=temp%10
    total+=digit**3
    temp//=10
print("Armstrong" if total==n else "Not Armstrong")
