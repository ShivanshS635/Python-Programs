f=open("Stock.txt","r")
a="READING DATA"
print(a.center(62,"*"))
s=f.read()
print(s)
f.close()

f=open("Stock.txt")
datalist=f.readlines()
f.close()

ic=input("Enter Item Code To Delete:")

for i,line in enumerate(datalist):
    l=line.split(",")
    if l[0]==ic:
        break
datalist.pop(i)
f=open("Stock.txt","w")
f.writelines(datalist)
f.close()

f=open("Stock.txt")
a="READING DATA AFTER DELETION"
print(a.center(62,"*"))
s=f.read()
print(s)
