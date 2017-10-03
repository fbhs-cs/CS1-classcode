'''
    Open dumbcalc.py

    Open Google Classroom
'''

import math

def find_c( a, b ):
    c = math.sqrt(a**2 + b**2)
    print('If a={} and b={} then c={:.2f}'.format(a,b,c))
    
side_a = float(input('Side a = '))
side_b = float(input('Side b = '))

find_c( side_a, side_b )



