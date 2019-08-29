import random
from Enviroment import Enviroment

# n = random.randint(min ,max)

##--------------------------------------
##-----------AGENTE---------------------
##--------------------------------------



class Agente_reactivo_simple:
    def __init__(self,env):
        self.puntos=0
        self.env = env
        print("--------------MAPA GENERADO---------------")
        self.env.print_enviroment()
        self.think()
    def up(self):
        self.env.init_posX -= 1
        return
    def down(self):
        self.env.init_posX += 1
        return
    def left(self):
        self.env.init_posY -= 1
        return
    def right(self):
        self.env.init_posY += 1
        return
    def suck(self):
        self.env.map[self.env.init_posX][self.env.init_posY] = "-"
        self.puntos+=1
        return
    def idle(self):
        return
    #def prespective(self,env):
    def think(self):

        while(self.env.accept_action()):



            if(self.env.init_posX == self.env.sizeX -1 and self.env.init_posY == self.env.sizeY  - 1 ):## Si termine el juego

                print("Limpieza finalizada")
                print("Se limpio ",self.puntos," de ",self.env.getAmount() , " de suciedad")
                print("Se utilizaron" , self.env.vidas," vidas")
                break
            if(self.env.init_posX  % 2 == 0 and self.env.init_posY != self.env.sizeY - 1 ):# par y extremo derecho
                print("derecha")
                self.right()
            elif(self.env.init_posX % 2 == 0 and self.env.init_posY == self.env.sizeY - 1):#par y fondo
                print("down")
                self.down()
            elif(self.env.init_posX % 2 != 0 and self.env.init_posY == 0 and self.env.init_posX != self.env.sizeX - 1):#impar y extremo izquierdo
                print("down")
                self.down()
            elif(self.env.init_posX %2 != 0  and self.env.init_posX == self.env.sizeX -1 ):
                print("right")
                self.right()
            else:
                print("left")
                self.left()

            if (self.env.if_dirty()):
                print("clean")
                self.suck()
            self.env.print_enviroment()
e = Enviroment(9,9,3,5,0.5)
a = Agente_reactivo_simple(e)