# print('Piškvorky')
# print('Hráč 1')
# print('Hráč 2')

field = []
class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def create_field(self):
        print(' ', end='')
        for width in range(self.width*self.height):
            print('',width, end='')
        print()
            
field = Field(3,3)
field.create_field()

# class Player:
#     def __init__(self, sign):
#         self.sign = sign
#         self._x = None
#         self._y = None
    
#     #Getters
#     @property
#     def x(self):
#         return self._x
    
#     @property
#     def y(self):
#         return self._y

#     #Setters
#     @x.setter
#     def x(self, x):
#         self._x = x
    
#     @y.setter
#     def y(self, y):
#         self._y = y
        

# player = Player("O")

# while True:
#     try:
#         player.x = int(input("Zadaj x-súradnicu: "))
#         player.y = int(input("Zadaj y-súradnicu: "))
#         if player.x in range(field.width) and player.y in range(field.height):
#             print("Správne súradnice")
#             break
#     except ValueError:
#         print("Nerozumiem")
    
#     print("Súradnice mimo rozsahu")    


# ROBIM COUNTER PRE KOLÁ - JEDNO KOLO OBIDVAJA HRÁČI ŤAHAJÚ, POSLEDNÉ KOLO BUDE ŤAHAŤ LEN JEDEN HRÁČ
# PRÁVE SOM DO3IEL NA TO ŽE HRACIU PLOCHU MUSÍM SPRAVIŤ CEZ LIST