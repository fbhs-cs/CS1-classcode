from math import ceil

print('+----+')
print('|    |')
print('|FBHS|')
print('|    |')
print('+----+')

school = 'abcdefgh'

print('+' + 20*'-' + '+')
print('|' + 20*' ' + '|')
print('|' + (10-len(school)//2)*' ' + school
      + (10-ceil(len(school)/2))*' ' + '|')
print('|' + 20*' ' + '|')
print('+' + 20*'-' + '+')
