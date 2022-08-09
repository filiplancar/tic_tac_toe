# print('Piškvorky')
# print('Hráč 1')
# print('Hráč 2')

# field = []
from itertools import count
from operator import index


empty_space = "_"
class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def create_field(self):
        self.field = [[f'{empty_space}' for w in range(self.width)] for h in range(self.height)]         

    def print_field(self):
        print(end="  ")
        for width in range(self.width):
            print(width, end=" ")
        print()
        for height, item in enumerate(self.field):
            print(height, " ".join(map(str, item)))

            
f = Field(3,3)
f.create_field()
f.print_field()

class Player:
    def __init__(self):
        self.sign = ["X", "O"]
        self._x = None
        self._y = None
    
    #Getters
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    #Setters
    @x.setter
    def x(self, x):
        self._x = x
    
    @y.setter
    def y(self, y):
        self._y = y
        

player = Player()

# print(f.field)

# while True:
#     try:
#         player.x = int(input("Zadaj x-súradnicu: "))
#         player.y = int(input("Zadaj y-súradnicu: "))
#         if player.x in range(f.width) and player.y in range(f.height):
#             field[(player.x+(player.x*2))+player.y] = f"{player.sign[0]} "
#             f.print_field()
#             break
#     except ValueError:
#         print("Nerozumiem")
    
#     print("Súradnice mimo rozsahu")    


#OGITOVAT KOD
#OINDEXOVAT POLE