from datetime import date
from datetime import datetime

tdate = date.today()
ttime = datetime.now()

def datefunc():
    d = tdate.strftime("%B %d, %Y")
    t = ttime.strftime("%H:%M:%S")
    if d == "December 24, 2019":
        print(d, end="")
        print("", t)
        print("Merry christmas!")
    else:
        print(d, end="")
        print("", t)

datefunc()