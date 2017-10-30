from random import randint

print('Welcome to the Magic Eight Ball')
print('Think of a yes/no question, then press <enter>')
input()
num = randint(1,3)
if num == 1:
    print('Yes, for sure.')
elif num == 2:
    print('No, absolutely not.')
elif num == 3:
    print('I can\'t tell for sure.')
    #TODO MORE RESPONSES
        # 1 MORE POSITIVE RESPONSE
        # 1 MORE UNSURE RESPONSE
        # 1 MORE NEGATIVE RESPONSE
        

    