class Dog:
    def __init__(self,breed,gender,age):
        self.breed = breed
        self.gender = gender
        self.age = age
        self.animal_type = "dog"

class Cat:
    def __init__(self,color,short_hair,gender,age):
        self.color = color
        self.short_hair = short_hair
        self.gender = gender
        self.age = age
        self.animal_type = "cat"

def main():
    my_dog = Dog("Cocker Spaniel","male",3)
    my_dog2 = Dog("Irish Wolfhound","female",1)
    print("Christian's dog:",my_dog.breed, my_dog.gender,my_dog.age)
    print("Ethan's dog:",my_dog2.breed, my_dog2.gender,my_dog2.age)

    hallies_cat = Cat("Orange",True,"male",2)
    print("Hallie's cat is",hallies_cat.color)
    
if __name__ == "__main__":
    main()