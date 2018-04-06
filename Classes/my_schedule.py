class Schedule:
    def __init__(self, first, second, third, fourth,\
                 fifth, sixth, seventh):
        self.schedule = (first, second, third, fourth,\
                         fifth, sixth, seventh)
        
    def morning(self):
        print(self.schedule[0],self.schedule[1],\
              self.schedule[2],self.schedule[3])

    def afternoon(self):
        print(self.schedule[4], self.schedule[5], self.schedule[6])
        
    def better_morning(self):
        for course in self.schedule[0:4]:
            print(course)
            
    def better_afternoon(self):
        for course in self.schedule[4:7]:
            print(course)

class Course:
    def __init__(self, name, instructor, room):
        self.name = name
        self.instructor = instructor
        self.room = room
    
    def __str__(self):
        return "{} - {} - Room {}".format(self.name,\
                                          self.instructor, self.room)
    
    
def main():
    # Create my classes
    cs = Course("Computer Science", "Mr. Perdy", 115)
    science = Course("Physics", "Mr. Wallase", 302)
    math = Course("Algebra", "Mr. Vallon", 803)
    geo = Course("World Geography", "Mr. Civils", 212)
    ela = Course("English", "Ms. Jonson", 510)
    art = Course("Art", "Ms. Lei", 108)
    span = Course("Spanish", "Ms. Gomez", 210)
    
    # Create my daily schedule
    my_schedule = Schedule(cs, math, geo, art, ela, span, science)
    
    # Print my morning and afternoon schedules
    # Notice the difference between how they are displayed
    print("My morning schedule:")
    my_schedule.morning()
    print()
    print("My afternoon schedule:")
    my_schedule.better_afternoon()
    print()
    
    # Access just a single period in my schedule
    print("My first period class is",my_schedule.schedule[0])
    print("My seventh period class is",my_schedule.schedule[6])
    
    
    # Let's say you decide to drop your 3rd period class
    # and replace it with an Office period...
    # Uncomment the line below and run the module
    
    #my_schedule.schedule[2] = Course("Office","Mr. Crenshaw","Office")

if __name__ == "__main__":
    main()