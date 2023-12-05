from FieldInhabitant import FieldInhabitant

# Creature class inheriting from FieldInhabitant
class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        super().__init__(symbol)
        self.__x = x
        self.__y = y
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x
    
    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__y = y
