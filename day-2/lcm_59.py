a=int(input())
b=int(input())
x=a
y=b
while y:
    x,y=y,x%y
print(abs(a*b)//x if x else 0)
