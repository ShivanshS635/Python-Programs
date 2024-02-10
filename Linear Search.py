###LINEAR SEARCH###

n=int(input("ENTER NUMBER OF ELEMENTS IN A LIST:"))
l=[]
p=0
for i in range (n):
    a=int(input("Enter :"))
    l.append(a)

def Search(l,m):
    for j in range (len(l)):
        if l[j]==m:
            global p
            p=j
            return True
    else:
        return False
    
m=int(input("ENTER NUMBER YOU WANT TO SEARCH:"))
if Search(l,m):
    print(m,"FOUND AT",p)
else:
    print(m,"NOT FOUND")
