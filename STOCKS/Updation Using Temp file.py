##f=open("Stock.txt","r")
##a="READING DATA"
##print(a.center(62,"*"))
##s=f.read()
##print(s)
##f.close()
##
##
##f=open("Stock.txt","r")
##t=open("Temp.txt","w")
##newline=input("Enter ItemCode,NewItemName,Rate,Quantity:")
##line=f.readline()
##while line!=" ":
##    l=line.split(",")
##    nl=newline.split(",")
##    if l[0]!=nl[0]:
##        t.write(line)
##    else:
##        t.write(newline)
##    line=f.readline()
##f.close()
##
##
##import os
##os.remove("Stock.txt")
##os.rename("Temp.txt","Stock.txt")
##
##
##f=open("Stock.txt","r")
##a="READING DATA AFTER UPDATION"
##print(a.center(62,"*"))
##s=f.read()
##print(s)
##f.close()

f=open("stock.txt")
print("Reading data from file:")
s=f.read()
print(s)
f.close()

f=open("stock.txt","r")
t=open("temp.txt","w")
newline=input("Enter icode,new iname,rate,qoh:")
line=f.readline()
while line!='':
    l=line.split(",")
    nl=newline.split(",")
    if l[0]!=nl[0]:
        t.write(line)
    else:
        t.write(newline+"\n")
    line=f.readline()
f.close()
t.close()

import os
os.remove("stock.txt")
os.rename("temp.txt","stock.txt")


f=open("stock.txt")
print("Reading data from file after updation:")
s=f.read()
print(s)
f.close()
