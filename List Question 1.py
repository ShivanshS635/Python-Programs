#FIND AND REPLACE
l=eval(input("ENTER ANY LIST:"))
n=int(input("ENTER VALUE TO FIND AND REPLACE:"))
r=int(input("ENTER REPLACING VALUE:"))
found=0
for i in range(len(l)):
    if l[i]==n:
        l[i]=r
        found=1
print(l)
        
if found==0:
    print("NO SUCH VALUE THERE IN LIST")
