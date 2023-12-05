#Name: Kshitij Patil 
#Date: 12/04/2023
#Description: Implementing the Snake Class

from Creature import Creature

class Snake(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "S")
