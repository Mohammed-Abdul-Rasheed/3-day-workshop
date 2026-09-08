def product(n):
    n=abs(n)
    if n<10:
        return n
    return n%10*product(n//10)

print(product(int(input())))
