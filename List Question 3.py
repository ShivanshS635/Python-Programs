l=eval(input("ENTER ANY LIST:"))
odd=0
even=0
for i in range(len(l)):
    if l[i]%2==0:
        l[i]=l[i]/2
        even=1
    else:
        l[i]=l[i]*2
        odd=1
print(l)
    
