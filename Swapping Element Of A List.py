l=eval(input("ENTER ANY LIST:"))
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)
