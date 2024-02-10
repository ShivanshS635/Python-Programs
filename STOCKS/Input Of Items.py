f=open("Stock.txt","a")
ch="Y"
while(ch.upper()=="Y"):
    line=input("ENTER RECORD(ITEMCODE,ITEMNAME,PRICE,QUANTITY):")
    f.write(line+"\n")
    ch=input("DO YOU WANT TO CONTINUE?(Y/N):")
f.close()
