#Name: Shreyak Godala
#Date: 12/04/2023
#Description: Implemention of the Captain class which inherits Creature class

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'V')
        self.__veggiesCollected = []

    def addVeggie(self, veggie):
        self.__veggiesCollected.append(veggie)


    def getVeggiesCollected(self):
        return self.__veggiesCollected




