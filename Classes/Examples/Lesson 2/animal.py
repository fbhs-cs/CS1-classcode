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
    donavins_dog = Dog("Boxer","female",3)
    print("Donavin's dog:",donavins_dog.breed,donavins_dog.gender,donavins_dog.age)   
    logans_dog = Dog("German Shephard","male",1)
    print("Logan's dog:",logans_dog.breed,logans_dog.gender,logans_dog.age)
    
    chases_cat = Cat("Grey",True,"male",6)
    print("Chase's cat is",chases_cat.color)

if __name__ == "__main__":
    main()