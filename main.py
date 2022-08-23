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
    
X = player.sign[0]
O = player.sign[1]

players = 2
round = 1
run = True

def chkList(lst):
    return len(set(lst)) == 1

p=0
while run:
    print(f"{round}. kolo")
    print(f"{p+1}. hráč")
    print()
    rewriting()
    print()

    diags1 = [r[i] for i, r in enumerate(f.field)]
    diags2 = [r[-i-1] for i, r in enumerate(f.field)]
    col = [col[0] for col in f.field]
    col1 = [col[1] for col in f.field]
    col2 = [col[2] for col in f.field]
    row = f.field[0]
    row1 = f.field[1]
    row2 = f.field[2]
    all_options = [diags1, diags2, col, col1, col2, row, row1, row2]
    
    for i in all_options:
        if chkList(i) == True and empty_space not in i:
            f.print_field()
            print(f"Vyhral {p+1}. hráč")
            run = False
            break
    
    if empty_space not in f.field:
        f.print_field()
        print(f"Remíza")
        run = False
        break
    
    p+=1
    if p == players:
        round+=1
        p = 0




#Zistiť prečo mi vypisuje vyhral hráč 1 a vyhral hráč 2 keď mám vyplnenú columns
#Musim zistit ako dostať row z f.field(Myslím že row = [f.field[0]])