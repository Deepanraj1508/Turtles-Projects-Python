import turtle
import time
from random import randint


for i in range (1,45):
    
    print('')

s=''

for i in range(1,1000):
    count = randint(1,100)
    while(count > 0):
        s += ' '
        count -= 1

    if (i%2==0):
        print(s + 'Kuttyma')
        print(s + 'I Love You Papa')
    else:
        print(s + '**')
        print(s + '~^~')
    s = ''
    time.sleep(0.1)
