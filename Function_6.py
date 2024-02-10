def palindrome(n):
    d=n
    a=0
    while(d!=0):
        c=d%10
        a=a*10+c
        d=d//10
    if(a==n):
        print(n,"IS A PALINDROME.")
    else:
        print(n,"IS NOT A PALINDROME.")
a=int(input("ENTER DIGIT:"))
palindrome(a)
