class List:
    def __init__(self):
        self.group = ('Eric Idle', 'John Cleese', 'Terry Jones', \
                      'Terry Gilliam', 'Michael Palin', ' Graham Chapman')
        
    def login(self, name):
        if name.title() in self.group:
            print('Hello' + ' ' + name.title())
        else:
            print('Invalid Login')
        
def main():
    pythons = List()
    pythons.login('eric idle')
    pythons.login('JOHN CLEESE')
    pythons.login('Harry Potter')
    pythons.login(input('Enter username >>'))
    
if __name__ == '__main__':
    main()


