base=int(input("Enter Basic Salary :"))
if base>10000:
    bonus=0.1*base
    print("Bonus:",bonus)
    total=base+bonus
    print("Total:",total)
else:
    bonus=0.05*base
    print("Bonus:",bonus)
    total=base+bonus
    print("Total:",total)
