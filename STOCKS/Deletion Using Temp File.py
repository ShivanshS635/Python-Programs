f=open("Stock.txt","r")
a="READING DATA"
print(a.center(62,"*"))
s=f.read()
print(s)
f.close()



f=open("Stock.txt","r")
t=open("Temp.txt","w")
ic=input("ENTER ITEM CODE TO DELETE:")
line=f.readline()
while line!="":
    l=line.split(",")
    if l[0] !=ic:
        t.write(line)
    line=f.readline()
f.close()
t.close()

import os
os.remove("Stock.txt")
os.rename("Temp.txt","Stock.txt")

f=open("Stock.txt")
a="READING DATA"
print(a.center(62,"*"))
s=f.read()
print(s)
f.close()

