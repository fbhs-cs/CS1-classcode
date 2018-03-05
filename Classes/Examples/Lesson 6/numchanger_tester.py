from numchanger import *

def main():
    test = NumChanger([1,3,5,7,9])
    print("Should print '1 3 5 7 9': ",test)
    test.add_to(6)
    print("Should print '7 9 11 13 15': ",test)
    print("Should print 'True': ",test.remove_from(11))
    print("Should print '7 9 13 15': ",test)
    print("Should print '44': ",test.get_sum())
    print("Should print '11.0': ",test.average())
    test.mult_to(3)
    print("Should print '21 27 39 45': ",test)
    
    test = NumChanger([1,1,2,2,3,3,4,4,4])
    print("Should print '4': ",test.mode())

if __name__ == "__main__":
    main()