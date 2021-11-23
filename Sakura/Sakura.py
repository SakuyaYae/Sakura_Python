"""
A class for createing a player
@author SakuyaYae
"""
class Sakura:
    #(Sakura note) Instans varable down below
    foucus = 100
    #(Sakura note) essensaly a constructor down below
    def __init__(self,hp, atk, armor, weapon, name, level):
        self.hp = hp
        self.atk = atk
        self.armor = armor
        self.weapon = weapon
        self.name = name
        self.level = level


    #(Sakura note) Instans metods down below
    #(Sakura note) eneables print on class object to show a string whit useful info
    def __str__(self):
        return f" name: {self.name} level: {self.level} HP: {self.hp} ATK: {self.atk} DEF: {self.armor} weapon: {self.weapon}"

    def attack(self, dmg):
        return f"{self.name} attacks for {dmg} on enemy"
