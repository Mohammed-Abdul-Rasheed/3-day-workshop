n=int(input())
digits=str(abs(n))
total=0
for digit in digits:
    total+=int(digit)**len(digits)
print("Armstrong" if total==abs(n) else "Not Armstrong")
