import time
import random

def slow_print(phrase):
    for i in range(len(phrase)):
        pause = 0
        #pause = random.random()/2
        print(phrase[i],end='',flush=True)
        time.sleep(pause)

line = 'Hello, my name is Douglas.\n'
slow_print(line)

line = "What's your name? "
slow_print(line)

name = input()
if len(name) > 10:
    slow_print('Oh, I just meant your first name...')
    if ' is ' in name:
        name = name[name.find(' is ')+4:]
        name = name[0].upper() + name[1:]
        slow_print('that\'s ok though, how are you today {}? '.format(name))
    
    elif ' ' in name:
        name = name.split()[0]
        name = name[0].upper() + name[1:]
        line = 'that\'s ok though, how are you today {}? '.format(name)
        slow_print(line)
    
    else:
        nicknames = ['sport','champ','boss','hoss']
        name = random.choice(nicknames)
        slow_print('That\'s ok though, how are you today {}? '.format(name))
  
elif ' ' in name:
        name = name.split()[0]
        name = name[0].upper() + name[1:]
        line = 'Hi there {}, how are you today? '.format(name)
        slow_print(line)

    
else:
    name = name[0].upper() + name[1:]
    line = 'Hi there {}, how are you today? '.format(name)
    slow_print(line)

how = input()
if 'fine' in how.lower() or 'good' in how.lower() or 'ok' in how.lower():
    slow_print('Well I\'m glad you\'re having a good day!\n')
    why = ''
elif 'great' in how.lower() or 'awesome' in how.lower() or 'terrific' in how.lower():
    slow_print('I\'m happy that you\'re happy!')
    why = ''
elif "i'm" in how.lower():
    line = 'Why are you {}? '.format(how[4:].lower())
    slow_print(line)
    why = input()
elif 'i am' in how.lower():
    slow_print('Why are you {}? '.format(how[5:].lower()))
    why = input()
elif 'bad' in how.lower() or 'sad' in how.lower() or 'terrible' in how.lower():
    slow_print("I'm sorry to hear that.  What's wrong? ")
    why = input()
else:
    slow_print('Why are you {}? '.format(how))
    why = input()

if why:
    if 'because' in why.lower() or "don't" in why.lower() or 'dont' in why.lower():
        slow_print('Well, if you don\'t want to talk about it...\n')
    else:
        slow_print('I see...')

while True:
    questions = ['So what else do you want to talk about today? ','What else is going on? ', 'Anything else? ', 'Care to share anything else? ', 'Any other news? '] 
    responses = ['Oh, how very interesting...', 'Well that\'s news to me...', 'You don\'t say...', "Thanks for sharing!", "I didn't know that..."]
    slow_print(random.choice(questions))
    whatelse = input()
    if 'nothing' in whatelse.lower() or 'nada' in whatelse.lower() or 'bye' in whatelse.lower() or 'not' in whatelse.lower() or 'no' in whatelse.lower():
        slow_print('Ok, well in that case, I gotta go.\n')
        break
    else:
        slow_print(random.choice(responses))

line = 'It was nice chatting!\nHave a great day, {}!\n'.format(name)
slow_print(line)
