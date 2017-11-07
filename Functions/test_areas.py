import areas

try:
    from areas import *
except:
    print('areas.py not found.')
    print('Are you in the right folder?')
    
def check_func(f,ival,rval,error=0):
    fname = f.__name__
    if(abs(f(ival) - rval)>error):
        print("Error in " + fname + "(" + str(ival) + ")")
        return False
        
    else:
        print(fname + "(" + str(ival)+")  OK")
        return True
        
def check_func2(f,i1val,i2val,rval,error=0):
    fname = f.__name__
    if(abs(f(i1val,i2val) - rval)>error):
        print("Error in " + fname + "(" + str(i1val) + ", " + str(i2val)+")")
        return False
        
    else:
        print(fname + "(" + str(i1val)+", " + str(i2val)+ ")  OK")
        return True

def check_func3(f,i1val,i2val,i3val,rval):
    fname = f.__name__
    if(f(i1val,i2val,i3val) != rval):
        print("Error in " + fname + "(" + str(i1val) + ", " + str(i2val)+ ", " + str(i3val) + ")")
        return False
    else:
        print(fname + "(" + str(i1val)+", " + str(i2val)+ ", " + str(i3val) + ")  OK") 
        return True


def main():
    num_tests = 0
    tests_passed = 0
    print("Testing area_square:")
    try:
        if check_func(area_square,5,25):
            tests_passed += 1
            
        if check_func(area_square,-5,0):
            tests_passed += 1
        
        if check_func(area_square,0,0):
            tests_passed += 1
    except:
        print('area_square not defined correctly')
    print("--------------------")
    print("Testing area_rectangle:")
    try:
        if check_func2(area_rectangle,5,6,30):
            tests_passed += 1
        if check_func2(area_rectangle,-5,6,0):
            tests_passed += 1
        if check_func2(area_rectangle,5,-6,0):
            tests_passed += 1
        if check_func2(area_rectangle,0,6,0):
            tests_passed += 1
    except:
        print('area_rectangle not defined correctly')
    print("--------------------")
    print("Testing area_parallelogram:")
    try:
        if check_func2(area_parallelogram,5,6,30):
            tests_passed += 1
        if check_func2(area_parallelogram,-5,6,0):
            tests_passed += 1
        if check_func2(area_parallelogram,5,-6,0):
            tests_passed += 1
        if check_func2(area_parallelogram,0,6,0):
            tests_passed += 1
    except:
        print('area_parallelogram not defined correctly')
    print("--------------------")
    print("Testing area_trapezoid:")
    try:
        if check_func3(area_trapezoid,2,4,6,18):
            tests_passed += 1
        if check_func3(area_trapezoid,-2,4,6,0):
            tests_passed += 1
        if check_func3(area_trapezoid,2,-4,6,0):
            tests_passed += 1
        if check_func3(area_trapezoid,2,4,-6,0):
            tests_passed += 1
        if check_func3(area_trapezoid,0,4,6,12):
            tests_passed += 1
    except:
        print('area_trapezoid not defined correctly')
    print("--------------------")
    print("Testing area_circle:")
    try:
        if check_func(area_circle,1,3.1415,.001):
            tests_passed += 1
        if check_func(area_circle,-2,0):
            tests_passed += 1
        if check_func(area_circle,0,0):
            tests_passed += 1
    except:
        print('area_circle not defined correctly')
    print("--------------------")
    print("Testing area_ellipse:")
    try:
        if check_func2(area_ellipse,5,6,94.2478,.001):
            tests_passed += 1
        if check_func2(area_ellipse,-5,6,0):
            tests_passed += 1
        if check_func2(area_ellipse,5,-6,0):
            tests_passed += 1
        if check_func2(area_ellipse,0,6,0):
            tests_passed += 1
    except:
        print('area_ellipse not defined correctly')
    print("--------------------")
    print("Testing area_triangle:")
    try:
        if check_func2(area_triangle,5,6,15):
            tests_passed += 1
        if check_func2(area_triangle,-5,6,0):
            tests_passed += 1
        if check_func2(area_triangle,5,-6,0):
            tests_passed += 1
        if check_func2(area_triangle,0,6,0):
            tests_passed += 1
    except:
        print('area_triangle not defined correctly')
    print("--------------------")
    print("Summary: {} tests passed out of 27 tests.".format(tests_passed))
    
if __name__ == "__main__":
    main()
