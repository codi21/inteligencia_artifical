import random
import math


def tablero_random(n):
    current_state = []
    for i in range(n):
        current_state.append(-1)
    j = 0
    while (j < n):
        ran = random.randint(0, n - 1)
        if current_state[ran] == -1:
            current_state[ran] = j
            j += 1
    return current_state

def cant_amenazas(vec):
    point = 0
    for i in range (len(vec)):
        j = 0
        while(j < len(vec)):
            if i != j :
                if (math.fabs(i - j) == math.fabs(vec[i] - vec[j])):
                    point += 1

            j+=1
    return point
def show_tablero(vec):
    for i in range(len(vec)):
        for j in range(len(vec)):
            if j == vec[i]:

                print("| @ |" ,end="")

            else:
                if j % 2 == 0 :
                    print("|___|",end="")
                else:
                    print("| ■ |",end="")
        print("")
def menor_amenaza(vec):
    menor = vec[0]
    menor2 = menor[2]

    for i in range(1,len(vec)):
        aux = vec[i]
        aux2 = aux[2]
        if aux2<menor2:
            menor = aux

    return menor
def hill_climbing(vec):
    ##cambiar la posicion i por todo el vector una vez que analizo el menor movimiento realizo el cambio caso contrario muevo el siguiente i
    iteracciones=0
    i = 0
    while iteracciones < 5 :
        if i == len(vec):
            i = 0
        amenazas = []
        amenazas.append((i,vec[i],cant_amenazas(vec)))


        for j in range(len(vec)):
            if i != j :

                aux = vec[i]
                vec[i] = vec[j]
                vec[j] = aux

                amenazas.append((i,j,cant_amenazas(vec)))
                vec[j]=vec[i]
                vec[i] = aux
        print("vector original",vec)
        print("vector amenaza",amenazas)
        less_tupla = menor_amenaza(amenazas)
        aux = vec[less_tupla[0]]

        vec[less_tupla[0]] = vec[less_tupla[1]]

        vec[less_tupla[1]] = aux
        print("desp de la modificacion",vec)
        if cant_amenazas(vec) == 0: #compruebo status goal
            return vec
        i+=1
        iteracciones+=1
    return vec
mejor = hill_climbing(tablero_random(14))
print("la mejor solucion es la siguiente",mejor,"con la cantidad de amenazas = ",cant_amenazas(mejor))