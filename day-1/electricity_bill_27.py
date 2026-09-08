units=int(input())
if units<=100:
    bill=units*1.5
elif units<=200:
    bill=150+(units-100)*2.5
else:
    bill=400+(units-200)*4
print(bill)
