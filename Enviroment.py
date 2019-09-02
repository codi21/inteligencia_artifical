import random




class Enviroment:

    def __init__(self, sizeX, sizeY, init_posX, init_posY, dirt_rate):
        # markdown acordarse
        self.sizeX = sizeX
        self.sizeY = sizeY
        random.seed(20)
        self.init_posX = random.randint(0, sizeX - 1)
        random.seed(20)
        self.init_posY = random.randint(0, sizeY - 1)
        self.dirt_rate = dirt_rate
        self.amount_dirty = 0
        #self.map = [range(sizeY) for i in range(sizeX)]
        self.map = []
        for i in range(sizeX):
            self.map.append([])
            for j in range(sizeY):
                self.map[i].append(0)
        self.vidas = 0
        self.ensuciar_map()




    def ensuciar_map(self):
        amount_dirt = round((self.sizeX*self.sizeY) *(self.dirt_rate )) ## cantidad de suciedad
        self.amount_dirty = amount_dirt
        random.seed(30)

        x_aleatorio = random.randint(0,self.sizeX-1)
        random.seed(30)
        y_aleatorio = random.randint(0,self.sizeY-1)
        while(amount_dirt > 0) :
            if(self.map[x_aleatorio][y_aleatorio] == 0):
                amount_dirt -= 1
            self.map[x_aleatorio][y_aleatorio] =  1
            x_aleatorio = random.randint(0, self.sizeX-1)
            y_aleatorio = random.randint(0, self.sizeY-1)

    def getAmount(self):
        return self.amount_dirty

    def accept_action(self,puntos):
        if(self.vidas == 1000):
            print("Limpieza finalizada")
            print("Se limpio ", puntos, " de ", self.getAmount(), " de suciedad")
            print("Se utilizaron", self.vidas, " vidas")
            return False
        else:
            self.vidas+= 1
            return True

    def if_dirty(self):
        if (self.map[self.init_posX][self.init_posY] == 1):
            return True
        else:
            return False

    # def get_perfomance(self):
    def getVidas(self):
        return self.vidas
    def print_enviroment(self):
        print("----------------------------------------------")
        print("----------------------------------------------")
        for i in range(self.sizeX):
            print("[" , end=" ")
            for j in range(self.sizeY):
                print(self.map[i][j] , end=" ")
            print("]")

