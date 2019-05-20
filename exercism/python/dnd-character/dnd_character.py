import math
import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """ returns sum of highest 3-of-4 6-sided dice rolls"""
        random.seed()
        rolls = [random.randint(1,6) for i in range(4)]
        return sum(sorted(rolls)[1:4])
    
def modifier(base):
    """returns down-rounded DND modifier"""
    return int(math.floor((base - 10) / 2))