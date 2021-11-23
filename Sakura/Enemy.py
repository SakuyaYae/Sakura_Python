"""
The class for createing an enemy
"""
class Enemy:
    def __init__(self, hp, atk, armor, weapon, name, level, type):
        self.hp = hp
        self.atk = atk
        self.armor = armor
        self.weapon = weapon
        self.name = name
        self.level = level
        self.type = type
    def __str__(self):
        return f" name: {self.name} enemy type: {self.type} level: {self.level} HP: {self.hp} ATK: {self.atk} DEF: {self.armor} weapon: {self.weapon}"
