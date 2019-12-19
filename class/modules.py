from random import choice
import os


tempList = ['a', 'b', 'c', 'd','e']
ch = choice(tempList)

for i in range(1,4):
    ch = choice(tempList)
    if not os.path.exists(ch):
        os.mkdir(ch)        
        os.chdir('./' + ch)
        print(os.getcwd())

