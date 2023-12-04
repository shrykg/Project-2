import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'V')
        self.__veggiesCollected = []

    def addVeggie(self, veggie):
        # Check if the passed object is an instance of Veggie
        # if isinstance(veggie, Veggie)
            self.__veggiesCollected.append(veggie)
        # else:
        #     print("Error: Only Veggie objects can be added to veggies_collected.")

    def getVeggiesCollected(self):
        return self.__veggiesCollected




