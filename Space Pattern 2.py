n=int(input(""))
sp=0
for i in range(n,0,-1):
    print()
    for j in range(1,i+1):
        print(j,end='')
    for j in range(sp):
        print(" ",end='')
    for j in range(i,0,-1):
        print(j,end='')
    sp+=2
