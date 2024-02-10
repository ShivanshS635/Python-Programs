import random
p1=input("Enter 1st Player's Name:")
p2=input("Enter 2nd Player's Name:")
sum1=0
sum2=0
while(True):

    a=random.randint(1,6)

    print(p1,"Gets",a)

    sum1=sum1+a

    b=random.randint(1,6)

    print(p2,"Gets",b)

    sum2=sum2+b

    print("Sum Of",p1,"Is:",sum1)

    print("Sum Of",p2,"Is:",sum2)

    if(sum1>=100):

        print(p1,"WINS")

        break

    elif(sum2>=100):

        print(p2,"WINS")

        break

        
