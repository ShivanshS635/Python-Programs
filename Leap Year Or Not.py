#WAP TO CHECK WEETHER IT IS LEAP YEAR OR NOT

year=int(input("Enter Thee Year:"))
a=year%4
if a==0:
    print(year,"Is A Leap Year")
else:
    print(year,"Is Not A Leap Year")
