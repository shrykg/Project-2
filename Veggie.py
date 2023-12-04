import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(self, symbol)
        self.__name = name
        self.__points = points

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPoints(self,points):
        self.__points = points

    def getPoints(self):
        return self.__points

    def getSymbol(self):
        return super().__symbol

    def __str__(self):
        print(f'{self.__symbol}: {self.__name} {self.__points} points')
