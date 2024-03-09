from time import time
from datetime import datetime

time = time()
#print(time)
print("Seconds since January 1, 1970:", "{:,.4f}".format(time), "or", "{:.2e}".format(time), "in scientific notation")

date = datetime.now()
day = date.strftime("%d")   #zero-padded day
month = date.strftime("%b") #truncated month
year = date.year
print(month, day, year)
