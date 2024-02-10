n=int(input("Enter Any Number:"))
for i in range(2,n):
    ch=0
    if(n%i==0):
        ch=1
        break
if(ch==0):
    print(n,"IS A PRIME NUMBER")
else:
    print(n,"IS NOT A PRIME NUMBER")
