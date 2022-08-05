# print('Piškvorky')
# print('Hráč 1')
# print('Hráč 2')
from turtle import width


field = []
empty_space = "_"
class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def create_field(self):
        for i in range(self.height*self.width):
            field.append(f'{empty_space} ')
            

    def print_field(self):
        index = 0
        print(" ", end = "")
        # for w in range(self.width):
        #     print("", w, end="")
            
        #     for h in range(self.height):
        #         print("\n", h)
        # print(" ")
        # for h,w in range in enumerate(field):
        # for axis in field:
        #     print("", index, end="")
        #     index += 1
        #     # if index == self.width:
        #     #     index = 0
        #     #     print("", field[index])
        for w in range(self.width):
            print("", w, end="")
        print()
        
        i = 0
        for index in range(len(field)):
            print(i,end=" ")
            while i != self.height+1:
                print(field[index],end="")
                i+=1
            i = 0
            print()
            
f = Field(3,3)
f.create_field()
# f.print_field()

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
            f.print_field()
            field[(player.x+(player.x*2))+player.y] = f"{player.sign[0]} "
            print(field)
            break
    except ValueError:
        print("Nerozumiem")
    
    print("Súradnice mimo rozsahu")    


# ROBIM COUNTER PRE KOLÁ - JEDNO KOLO OBIDVAJA HRÁČI ŤAHAJÚ, POSLEDNÉ KOLO BUDE ŤAHAŤ LEN JEDEN HRÁČ
# DOŠIEL SOM NA TO ŽE POLE MUSÍM SPRAVIŤ NEJAKO CEZ FOR CYKLUS, CEZ DVA FOR CYKLY - NAJSKOR VYRIESIM ABY SA MI VYPISOVALI INDEXY
#FOR CYKLY BY MALI BYŤ PREPOJENÉ SPOLU V PRINT_FIELD