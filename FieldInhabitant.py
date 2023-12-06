#Name: Shreyak Godala
#Date: 12/04/2023
#Description: Implemention of the FieldInhabitant which is the most Super class in this project
class FieldInhabitant:
    def __init__(self, symbol):
        self.__symbol = symbol

    def getSymbol(self):
        return self.__symbol

    def setSymbol(self, symbol):
        self.__symbol = symbol
