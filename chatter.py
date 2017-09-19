import time
def slow_print(phrase):
    for i in range(len(phrase)):
        print(phrase[i],end='',flush=True)
        time.sleep(0.25)

line = 'What is your name? '
slow_print(line)

name = input()

line = 'Hi there {}, how are you today? '.format(name)
slow_print(line)

how = input()

line = 'Why are you {}? '.format(how)
slow_print(line)

why = input()

print('Oh, how interesting.',end='',flush=True)
for i in range(8):
    time.sleep(1)
    print('.',end='',flush=True)

line = 'Well, have a great day, {}!\n'.format(name)
slow_print(line)
