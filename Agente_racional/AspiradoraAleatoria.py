import random
from Enviroment import Enviroment

class AspiradoraAleatoria:
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
        #pcdiscount
        while(self.env.accept_action(self.puntos)):
            if (self.env.if_dirty()):
                print("clean")
                self.suck()
            n = random.randint(0, 3)
            if(n == 0):
                if(self.env.init_posX != 0):
                    self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                    self.up()
                else:
                    continue
            elif(n == 1 ):
                if(self.env.init_posX != self.env.sizeX-1 ):
                    self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                    self.down()
                else:
                    continue
            elif(n == 2):
                if(self.env.init_posY != self.env.sizeY-1):
                    self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                    self.right()
                else:
                    continue
            elif(n == 3):
                if(self.env.init_posY != 0):
                    self.env.map[self.env.init_posX][self.env.init_posY] = "*"
                    self.left()
                else:
                    continue
            self.env.print_enviroment()
            print("Limpieza finalizada")
            print("Se limpio ", self.puntos, " de ", self.env.getAmount(), " de suciedad")
            print("Se utilizaron",self.env.vidas)

e = Enviroment(64,64,0,0,0.4)
a = AspiradoraAleatoria(e)