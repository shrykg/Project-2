#Name: Shreyak Godala
#Date: 12/04/2023
#Description: Implemention of the Rabbit class which inherits Creature class

from Creature import Creature
class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'R')



