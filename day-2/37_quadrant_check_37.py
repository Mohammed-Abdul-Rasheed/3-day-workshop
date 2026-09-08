x=float(input())
y=float(input())
if x>0 and y>0:
    print("First Quadrant")
elif x<0 and y>0:
    print("Second Quadrant")
elif x<0 and y<0:
    print("Third Quadrant")
elif x>0 and y<0:
    print("Fourth Quadrant")
else:
    print("On Axis")
