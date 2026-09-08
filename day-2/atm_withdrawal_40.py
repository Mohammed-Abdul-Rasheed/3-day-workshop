amount=float(input())
balance=float(input())
minimum=float(input())
print("Approved" if amount>0 and amount<=balance-minimum else "Rejected")
