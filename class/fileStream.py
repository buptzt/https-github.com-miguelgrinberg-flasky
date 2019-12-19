import os
import sys


num = int (sys.argv[1])
if num % 2 == 0:
    print("input error! exit")
    sys.exit(0) 
  
f = open('./stars.txt','w+')

for i in range (0, num/2 + 1 ):
    str = ' ' * (num/2 - i) + '*' * (i*2+1) + '\n'
    f.write(str)

for i in range(1, num/2 + 1):
    str = ' ' * i + '*' * (num- 2* i)+ '\n'
    f.write(str)

f.close()

os.system('cat stars.txt')
