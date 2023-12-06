#Name: Shreyak Godala
#Date: 12/04/2023
#Description: Implemention of the Veggie class which inherits FieldInhabitant class


from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
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
        return super().getSymbol()

    def __str__(self):
        return f'{self.getSymbol()}: {self.__name} {self.__points} points'
