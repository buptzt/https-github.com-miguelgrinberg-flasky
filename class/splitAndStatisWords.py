import os
import sys
import re

dict = {}

fp = open('./hello.txt', 'r')

for line in fp.readlines():
    line = line.rstrip()
    print('line:%s'%line)

    for it in re.split(r' |;|,',line):
        if dict.has_key(it):
            dict[it] += 1
        else:
            dict[it] = 1

fp.close()
   
for key,value  in dict.items():
    print("%s:%d" %(key,value))

