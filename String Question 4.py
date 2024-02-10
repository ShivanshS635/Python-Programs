a=input("Enter Any String:")
n=len(a)
x=a[0:2]
y=a[2:n-2]
z=a[n-2:]
if(n>2):
    print("Real:",a)
    print("Fake:",z+y+x)
else:
    print("ERROR".center(25,"!"))
    print("Given String Is <=2")
