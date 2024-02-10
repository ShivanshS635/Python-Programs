f=open("Stock.txt")
datalist=f.readlines()
sum=0
ctr=1
for line in (datalist):
    l=line.rstrip().split(",")
    print(ctr,":",l)
    ctr+=1
f.close()
