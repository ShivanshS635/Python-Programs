s=input("ENTER ANY STRING:")
l=[]
for i in s :
    if i.isdigit():
        l.append(i)
a="".join(l)
print(a)
