n=int(input())
prime=n>1
i=2
while i*i<=n:
    if n%i==0:
        prime=False
        break
    i+=1
print("Prime" if prime else "Not Prime")
