# print('Piškvorky')
# print('Hráč 1')
# print('Hráč 2')
field = []
empty_space = "_"
class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def create_field(self):
        print(" ", end = "")
        for w in range(self.width):
            print("", w, end="")
        
        print(" ")
        for h in range(self.height):
            field.append(f'{empty_space} '*self.width)
            print(h, field[h])
            
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

while True:
    try:
        player.x = int(input("Zadaj x-súradnicu: "))
        player.y = int(input("Zadaj y-súradnicu: "))
        if player.x in range(f.width) and player.y in range(f.height):
            print("Správne súradnice")
            break
    except ValueError:
        print("Nerozumiem")
    
    print("Súradnice mimo rozsahu")    


# ROBIM COUNTER PRE KOLÁ - JEDNO KOLO OBIDVAJA HRÁČI ŤAHAJÚ, POSLEDNÉ KOLO BUDE ŤAHAŤ LEN JEDEN HRÁČ
# DOŠIEL SOM NA TO ŽE POLE MUSÍM SPRAVIŤ NEJAKO CEZ FOR CYKLUS, CEZ DVA FOR CYKLY - NAJSKOR VYRIESIM ABY SA MI VYPISOVALI INDEXY