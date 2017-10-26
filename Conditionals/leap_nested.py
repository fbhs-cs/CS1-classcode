year = int(input('Enter a year: '))
is_leap_year = False

if year > 2017: 
    if year % 400 == 0:
        is_leap_year = True
    elif year % 4 == 0:
        if year % 100 != 0:
            is_leap_year = True
        
            
    if is_leap_year:
        print('{} will be a leap year.'.format(year))
    else:
        print('{} will not be a leap year.'.format(year))
    
else:
    if year % 400 == 0:
        is_leap_year = True
    elif year % 4 == 0:
        if year % 100 != 0:
            is_leap_year = True

    if is_leap_year:
        print('{} was a leap year.'.format(year))
    else:
        print('{} was not a leap year.'.format(year))

        
