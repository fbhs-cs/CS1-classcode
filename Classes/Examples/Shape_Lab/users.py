class List:
    def __init__(self):
        self.group = ("Eric Idle", "John Cleese", "Terry Jones",
                      "Terry Gilliam", "Michael Palin",
                      "Graham Chapman")
    
    def login(self, name):
        # print out hello to the member of the group if
        # the name is equal to any member of the group
        # make the name non case-sensitive
        # if they are not in the group print "Invalid login."
        for member in self.group:
            if name.lower() == member.lower():
                print("Hello",name.title())
                break
            
        else:
            print("Invalid login.")
        
def main():
    pythons = List()
    pythons.login("eric idle")          # Hello Eric Idle
    pythons.login("JOHN CLEESE")        # Hello John Cleese
    pythons.login("Harry Potter")       # Invalid login.
    pythons.login(input("Enter user name >>"))
        # the result of the final login depends on what you choose
        # to have the user type in.

if __name__ == "__main__":
    main()