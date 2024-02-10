p=int(input("Enter Principle Amount:"))
r=int(input("Enter Rate:"))
t=int(input("Enter Time:"))
ci=p*(1+r/100)**t
print("Compound Interest:",ci)
