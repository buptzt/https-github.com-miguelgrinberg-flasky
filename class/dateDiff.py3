import time
import sys
import datetime


print(sys.argv[0])

try:
    str1= input("please input the date1:")
    str = str1 + " " + "00:00:00"
    date1 = time.strptime(str, '%Y-%m-%d %H:%M:%S')
except:
    print("date time %s does not math format \'%Y-%m-%d\'")

try:
    str2= input("please input the date2:")
    str = str2 + " " + "00:00:00"
    date2 = time.strptime(str, '%Y-%m-%d %H:%M:%S')
except:
    print("date time %s does not math format \'%Y-%m-%d\'")

print(date1)
print(date2)
d1 = datetime.datetime(date1.tm_year, date1.tm_mon, date1.tm_mday)
d2 = datetime.datetime(date2.tm_year, date2.tm_mon, date2.tm_mday)
print((d2-d1).days)


