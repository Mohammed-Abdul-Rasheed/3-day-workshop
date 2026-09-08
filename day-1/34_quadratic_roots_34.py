import cmath
a=float(input())
b=float(input())
c=float(input())
d=b*b-4*a*c
print((-b+cmath.sqrt(d))/(2*a))
print((-b-cmath.sqrt(d))/(2*a))
