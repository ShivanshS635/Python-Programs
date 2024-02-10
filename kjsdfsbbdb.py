n=int(input())
for i in range(1,n+1):
    c=ord("A"+i-1)
    for j in range(j,i+1):
        print(chr(c+j-1))
    print()
