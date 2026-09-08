total=0
count=0
while True:
    n=float(input())
    if n==-1:
        break
    total+=n
    count+=1
print(count)
print(total/count if count else 0)
