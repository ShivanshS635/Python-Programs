s1=int(input("Enter Score Of Maths:"))
s2=int(input("Enter Score Of Physics:"))
s3=int(input("Enter Score Of Chemistry:"))

perc=(s1+s2+s3)/3
print(perc)
if(perc>=75):
    print("Distinction")
elif(75>perc>=60):
    print("First Division")
elif(60>perc>=50):
    print("Second Division")
else:
    print("Fail")
