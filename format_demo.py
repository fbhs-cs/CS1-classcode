name = input('What is your name? ')

print('Hello ' + name + ' I hope you had a nice weekend!')
print('Well, {} I have a few more questions for you...'.format(name))

print()

print('This line of text ',end='')
print('and this line of text ',end='')
print('appear on the same line!')

print()

num_classes = input('How many classes are you taking this year? ')
print("Wow {}! {} is a LOT of classes.  I bet you're busy!".format(name,num_classes))
print("Don't worry {}, I took {} classes ".format(name, num_classes),end='')
print('one year and look at how I turned out!')

fav_class = input('What is your favorite class, {}? '.format(name))
print("Oh, well I never really liked {}.".format(fav_class))
