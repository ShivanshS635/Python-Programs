import random
a=random.randint(1,10)
print(a)
win=0
for i in range(3):
    b=int(input("Guess Number Between 1-10:"))
    if(b<a):
        print("Entered Number Is Less Than Real One")
    elif(a<b):
        print("Entered Number Is More Than Real One")
    elif(a==b):
        print("You Win")
        win=1
        break
if win==0:
    print("You Lose")
    


