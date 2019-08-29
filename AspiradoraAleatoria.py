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
        while(self.env.accept_action()):
            n = random.randint(0, 3)
            if(n == 0):
                if(self.env.init_posX != 0):
                    self.up()
                else:
                    continue
            elif(n == 1 ):
                if(self.env.init_posX != self.env.sizeX-1 ):
                    self.down()
                else:
                    continue
            elif(n == 2):
                if(self.env.init_posY != self.env.sizeY-1):
                    self.right()
                else:
                    continue
            elif(n == 3):
                if(self.env.init_posY != 0):
                    self.left()
                else:
                    continue
            if (self.env.if_dirty()):
                print("clean")
                self.suck()
            self.env.print_enviroment()
            print("Limpieza finalizada")
            print("Se limpio ", self.puntos, " de ", self.env.getAmount(), " de suciedad")
            print("Se utilizaron",self.env.vidas)

e = Enviroment(9,9,3,5,0.5)
a = AspiradoraAleatoria(e)