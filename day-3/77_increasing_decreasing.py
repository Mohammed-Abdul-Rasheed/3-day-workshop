def print_numbers(current,n):
    if current>n:
        return
    print(current)
    print_numbers(current+1,n)
    print(current)

n=int(input())
print_numbers(1,n)
