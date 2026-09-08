x=float(input())
n=int(input())
total=0
factorial=1
power=x
for i in range(n):
    if i>0:
        power*=x*x
        factorial*=(2*i)*(2*i+1)
    total+=power/factorial if i%2==0 else -power/factorial
print(total)
