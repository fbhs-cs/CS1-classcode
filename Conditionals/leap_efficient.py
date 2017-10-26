year = int(input('Enter a year: '))
is_leap_year = False

if year > 2017: 
    y = 'will be'
    n = 'will not be'
else:
    y = 'was'
    n = 'was not'

if year % 400 == 0:
    is_leap_year = True
elif year % 4 == 0 and year % 100 != 0:
        is_leap_year = True      
            
if is_leap_year:
     print('{} {} a leap year.'.format(year,y))
else:
     print('{} {} a leap year.'.format(year,n))
    

        
