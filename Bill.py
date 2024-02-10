pr=int(input("Enter Previous Reading:"))
nr=int(input("Enter New Reading:"))
rpu=int(input("Enter Rate Per Unit:"))
uc=nr-pr
bill=uc*rpu
print("Unit consumed:",uc)
print("Bill :",bill)
