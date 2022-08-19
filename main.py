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

def rewriting():
    try:
        f.print_field()
        player.x, player.y  = int(input("Zadaj x-súradnicu: ")), int(input("Zadaj y-súradnicu: "))

        if player.x in range(f.width) and player.y in range(f.height) and f.field[player.x][player.y] == empty_space:
           f.field[player.x][player.y] = player.sign[p]
                    
        else:
            print("Zlé súradnice")  
            rewriting()
    except ValueError:
        print("Nerozumiem")    
        rewriting()
    
players = 2
round = 1
run = True

while run:
    for p in range(players):
        if empty_space not in f.field:
            f.print_field()
            run = False
        
        else:
            print(f"{round}. kolo")
            print(f"{p+1}. hráč")
            print()
            rewriting()
            print()
    round+=1

#Už som vyriešil to aby sa mi menili kolá
#Teraz treba vyriešiť to aby sa mi nič nepripočítavalo keď dám zlú súradnicu
