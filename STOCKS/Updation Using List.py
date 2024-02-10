f=open("Stock.txt","r")
a="READING DATA"
print(a.center(62,"*"))
s=f.read()
print(s)
f.close()


f=open("Stock.txt")
datalist=f.readlines()
f.close()

newline=input("Enter ICode,NewItemName,Rate,Quantity:")

for i,line in enumerate(datalist):

    nl=newline.split(",")
    l=newline.split(",")
    if l[0]==nl[0]:
        break

datalist.pop(i)
datalist.insert(i,newline+"\n")
f.close()

f=open("Stock.txt","w")
f.writelines(datalist)
f.close()

f=open("Stock.txt","r")
a="READING DATA AFTER UPDATION"
print(a.center(60,"*"))
s=f.read()
print(s)
f.close()
