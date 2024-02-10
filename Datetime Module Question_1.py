from datetime import datetime,date,time,timedelta
d=date.today()
y=d-timedelta(days=1)
t=d+timedelta(days=1)
print("YESTERDAY'S DATE:",y)
print("TOMORROW'S DATE:",t)
