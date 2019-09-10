import math
import random


def amenazas(pos_x,pos_y,vec): ## dada una pos y un vector , contabilizo la cant de amenazas
    point=0
    for i in range(len(vec)):
        if(i != pos_y or vec[i] != pos_x):
            if(math.fabs(pos_y- i ) == math.fabs(pos_x - vec[i])):
                point+=1
            if(i == pos_y):
                point+=1
            if(pos_x == vec[i]):
                point+=1
    return point
def printMatriz(m):
    for i in range(len (m)):
        print("[",end="")
        for j in range(len(m)):
            print(m[i][j], end=",")
        print("]")
        print("\n")
def minimo_matriz(matriz):#Busca el min de la matriz para proceder a hacer el movimiento de la ficha
    min=matriz[0][0]
    indice=(0,0)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(matriz[i][j]< min):
                min = matriz[i][j]
                indice=(i,j)
    return indice
def heuristica(state): ## Devuelve un mejor estado haciendo un solo movimiento
    matriz=[[None] * len (state) for i in range(len(state))]
    for i in range(len(state)): ## Coloco 1000 donde estan ubicadas las fichas
        matriz[state[i]][i] = 1000

    for i in range (len(state)): ## Voy colocando la cantidad de amenazas que tienen las fichas dado un supuesto movimiento
        for j in range(len(state)):
            if(matriz[i][j] != 1000):
                state[i] = j
                matriz[i][j] = sumas_amenazas(state)

    x = minimo_matriz(matriz) ## elijo el mejor movimiento
    state[x[1]]=x[0] ## realizo el movimiento de ficha
    return state  ## Devuelvo el nuevo estado

def sumas_amenazas(vec):## cantidad de amenazas de cada estado
    sum = 0
    for i in range(len(vec)):
        sum+=amenazas(vec[i],i,vec)
    return sum

def hill_climb(n): ## Recibimos el tamaño del tablero
    ##Definiendo current state
    current_state=[]
    for i in range(n):
        current_state.append(random.randint(0,n-1))
    goal_state = False
    movements = 0
    ## Loop hasta que encuentre el estado ideal (en mi caso que la cantidad de amenzas de cada reina sea = a 0)
    ## o llegue al limite de movimientos osea = a 1000
    current_state2 =[]
    while(goal_state == False and movements < 1000 ):
        current_state2 = current_state.copy()
        print("current state " , current_state)
        print("el current state tiene ",sumas_amenazas(current_state2)," amenazas")
        new_state = heuristica(current_state)##apartir del tablero generado por la heuristica elegida , elijo un nuevo estado.
        print("Sale new state " , new_state," con ",sumas_amenazas(new_state),"cantidad de amenazas")
        if(sumas_amenazas(new_state)== 0): ##Si llego al estado ideal ( Donde las fichas no tienen amenazas )
            current_state= new_state
            goal_state =True
        elif(sumas_amenazas(new_state) >= sumas_amenazas(current_state2)): ## Si el nuevo estado es peor que el que tenia
            return current_state2
        else :
            movements+=1
            current_state = new_state ##Si encontre un estado mejor
    return current_state ##Devuelvo el mejor estado encontrado




a = hill_climb(8)
print(a)