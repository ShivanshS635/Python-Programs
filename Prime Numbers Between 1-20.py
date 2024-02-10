for i in range(2,21):
    ch=0
    for j in range(2,i):
        if(i%j==0):
            ch=1
            break
    if(ch==0):
        print(i)

    
