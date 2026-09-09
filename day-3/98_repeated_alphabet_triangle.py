n=int(input())
for i in range(n):
    letter=chr(65+i)
    print(" ".join([letter]*(i+1)))
