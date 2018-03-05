class Hero:
    def __init__(self, weapon):
        self.alive = True
        self.weapon = weapon
        self.level = 1
        
    def attack(self):
        self.weapon.power -= 5
        
class Weapon:
    def __init__(self, style, power):
        self.style = style
        self.power = power
    
    def __str__(self):
        return "Weapon: {} \nPower: {}".format(self.style, self.weapon)
    
    