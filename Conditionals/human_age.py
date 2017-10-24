age = float(input("How old is the human? "))
term = 'unknown'

if age < 0 or age > 150:
    print("That's unlikely.")
    term = 'improbable'

if age >= 0 and age < 1:
    term = 'baby'
if age >= 1 and age < 3:
    term = 'toddler'
if age >= 3 and age < 5:
    term = 'preschooler'
if age >= 5 and age < 9:
    term = 'child'
if age >= 9 and age < 13:
    term = 'preteen'
if age >= 13 and age < 18:
    term = 'teen'
if age >= 18 and age < 40:
    term = 'young adult'
if age >= 40 and age < 65:
    term = 'adult'
if age >= 65:
    term = 'elderly'

if term == 'unknown':
    print("You did something wrong, but I'm not sure what.")
if term != 'unknown':
    print("A human {} years old is usually called '{}'.".format(age, term))