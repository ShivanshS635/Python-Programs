#TO FIND OCCURENCE IN FORM OF DICTIONARY
l=eval(input("ENTER ANY LIST:"))
d={}
for item in l:
    d[item]=d.get(item,0)+1
        ##or
        ##d[item]=1
##    else:
        ##d[item]+=1
print(d)
