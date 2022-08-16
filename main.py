# print('Piškvorky')
# print('Hráč 1')
# print('Hráč 2')

# field = []
from shutil import move
import numpy as np
empty_space = "_"
class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def create_field(self):
        self.field = np.array([[f'{empty_space}' for w in range(self.width)] for h in range(self.height)])         

    def print_field(self):
        print(end="  ")
        for width in range(self.width):
            print(width, end=" ")
        print()
        for height, item in enumerate(self.field):
            print(height, " ".join(map(str, item)))

f = Field(3,3)
f.create_field()
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

def swap_players(ndx):
    return players[(ndx+1)%len(players)]

players = [2,1]

for move in range(f.width*f.height):
    p = swap_players(move)
    print(f"{p}. hráč")
    f.print_field()
    try:
        player.x, player.y  = int(input("Zadaj x-súradnicu: ")), int(input("Zadaj y-súradnicu: "))
        if player.x in range(f.width) and player.y in range(f.height) and f.field[player.x][player.y] == empty_space:
            f.field[player.x][player.y] = player.sign[p-1]
            
        else:
            print("Zlé súradnice")         
    except ValueError:
        print("Nerozumiem")    


#Mením empty space na X, O 
#RIEŠIM TO ABY SA MI MENILI HRÁČI
