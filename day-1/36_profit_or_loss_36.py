cost=float(input())
selling=float(input())
if selling>cost:
    print("Profit",selling-cost)
elif selling<cost:
    print("Loss",cost-selling)
else:
    print("No Profit No Loss")
