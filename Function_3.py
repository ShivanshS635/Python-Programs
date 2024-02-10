def nod(m,y):
    if y%4==0:
        if  m.capitalize()=="February":
            return "29"
        elif m.capitalize() in ["January","March","May","July","September","November"]:
            return  "31"
        elif m.capitalize() in ["April","June","August","October","December"]:
            return "30"
    else:
        if  m.capitalize()=="Februray":
            return "28"
        elif m.capitalize() in ["January","March","May","July","August","October","December"]:
            return  "31"
        elif m.capitalize() in ["April","June","August","October","December"]:
            return "30"
m=input("ENTER MONTH:")
y=int(input("ENTER YEAR :"))
c=nod(m,y)
print(c)
        
