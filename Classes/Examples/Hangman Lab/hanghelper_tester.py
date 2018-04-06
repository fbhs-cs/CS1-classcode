from hanghelper import *

try:
    print("Trying rand_word()")
    for i in range(5):
        w = rand_word()
        print(w,len(w))
except Exception as e:
    print("rand_word not working:",e)

input('Press enter to test print_man')
try:
    print("testing print_man")
    for i in range(8):
        print_man(i)
except Exception as e:
    print("print_man not working",e)