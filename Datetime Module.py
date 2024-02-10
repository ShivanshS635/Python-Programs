##from datetime import datetime,date,time,timedelta
####currentdate
####d=date.today()
####print("TODAY IS :",d)
####print(d.year,d.month,d.day)
####print(d.weekday())
####l=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
####print(l[d.weekday()])
##
##
####current date and time
####a=datetime.now()
####print(a)
####print(a.strftime("%a %d %b %y"))
####print(a.strftime("%x"))
##
##
####time delta
####d=datetime.now()
####nd=d+timedelta(days=5)
####print(nd)
##
##
####day  after 5 days
####td=date.today()
####fd=date(td.year,1,1)
####print((td-fd).days)
##
##
###string to date
##
##s=input("ENTER DATE (DD-MM-YYYY ):")
##d=datetime.strptime(s,"%d - %m - %Y")
##print(d)
##
##
##
