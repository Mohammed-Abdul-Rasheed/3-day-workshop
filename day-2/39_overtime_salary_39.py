hours=float(input())
rate=float(input())
if hours>40:
    print(40*rate+(hours-40)*rate*1.5)
else:
    print(hours*rate)
