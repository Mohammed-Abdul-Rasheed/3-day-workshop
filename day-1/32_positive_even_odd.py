n=int(input())
if n>0:
    print("Positive Even" if n%2==0 else "Positive Odd")
elif n<0:
    print("Negative")
else:
    print("Zero")
