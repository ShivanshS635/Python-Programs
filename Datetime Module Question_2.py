from datetime import datetime,date,time,timedelta
d=date.today()
for i in range(1,6):
    print(d+timedelta(days=i))
