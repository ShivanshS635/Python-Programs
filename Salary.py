base=int(input("Enter Base Salary:"))
hra=int(input("Enter HRA:"))
da=int(input("Enter DA:"))
gross=base+hra+da
print("Gross:",gross)
pf=int(input("Enter PF:"))
net=gross-pf
print("Net Salary:",net)
