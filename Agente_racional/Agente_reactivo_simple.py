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
        print("cantidad de suciedad",self.env.getAmount())
        while(self.env.accept_action(self.puntos)):
            if (self.env.if_dirty()):
                print("clean")
                self.suck()
            if(self.env.init_posX == self.env.sizeX -1 and self.env.init_posY == self.env.sizeY  - 1 ):## Si termine el juego
                print("Limpieza finalizada")
                print("Se limpio ",self.puntos," de ",self.env.getAmount() , " de suciedad")
                print("Se utilizaron" , self.env.vidas," vidas")
                break
            if(self.env.init_posX  % 2 == 0 and self.env.init_posY != self.env.sizeY - 1 ):# par y extremo derecho
                self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                print("derecha")
                self.right()

            elif(self.env.init_posX % 2 == 0 and self.env.init_posY == self.env.sizeY - 1):#par y fondo
                self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                print("down")
                self.down()

            elif(self.env.init_posX % 2 != 0 and self.env.init_posY == 0 and self.env.init_posX != self.env.sizeX - 1):#impar y extremo izquierdo
                self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                print("down")
                self.down()

            elif(self.env.init_posX %2 != 0  and self.env.init_posX == self.env.sizeX -1 ):
                self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                print("right")
                self.right()

            else:
                self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                print("left")
                self.left()
            self.env.print_enviroment()
e = Enviroment(128,128,0,0,0.8)
a = Agente_reactivo_simple(e)