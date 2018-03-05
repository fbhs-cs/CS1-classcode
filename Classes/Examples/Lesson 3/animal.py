class Dog:
    def __init__(self, breed, gender, age):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.animal_type = "dog"
        
    def bark(self,amount):
        for i in range(amount):
            print("BARK!")
            
def main():
    pup = Dog("poodle","female",2)
    print("pup should bark 4 times:")
    pup.bark(4)
    print("pup should bark 8 times:")
    pup.bark(8)

if __name__ == "__main__":
    main()