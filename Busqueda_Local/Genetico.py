import math
import random
import time
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
def pertenece(n , list):
    for i in range(len(list)):
        if n == list[i]:
            return True

    return False

def buscar(i ,padre,sublist):
    while True :
        if i == len(padre):
            i = 0
        if pertenece(padre[i],sublist):
            i+=1
        else :
            s = padre[i]
            padre[i] = sublist[0]
            return s

def cross_over_en_orden(padre , madre):
    x = random.randint(0,len(padre)-1)
    y = random.randint(x,len(madre)-1)
    offspring1=[-1 for i in padre]
    sublist1 = []
    offspring2=offspring1.copy()
    sublist2=[]
    for i in range(len(padre)):
        if i >= x and i<= y :
            offspring1[i]= padre[i]
            sublist1.append(padre[i])
            offspring2[i] = madre[i]
            sublist2.append(madre[i])

    i = y
    while True :
        i += 1
        if i >= len(padre):
            i = 0
        if i == x :
            break
        j = i
        new_n = buscar(j , madre ,sublist1)
        offspring1[i]= new_n
        new2 = buscar(j,padre,sublist2)
        offspring2[i]=new2
    solution=[]
    solution.append(offspring1)
    solution.append(offspring2)
    return solution
def mutacion(list):
    cant_genes = random.randint(0,len(list)-1)
    for i in range(cant_genes):
        x = random.randint(0,len(list)-1)
        y = random.randint(0,len(list)-1)
        aux = list[x]
        list[x]=list[y]
        list[y]=aux
    return list
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
def generar_poblacion(n):
    p = []
    for i in range(150):
        p.append(tablero_random(n))

    return p
def calcular_fitness(p):
    fit =[]
    for i in range(len(p)):
        fit.append((cant_amenazas(p[i]),i))
    return fit

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

def seleccion(p):
    fit = calcular_fitness(p)
    fit.sort()
    new_p = []
    if len(p) <= 2:
        return p
    for i in range(len(p)-2):
        new_p.append(p[fit[i][1]])
    return new_p
def cross_poblation(p):
    new_p = []
    for i in range(0,len(p),2):
        l= cross_over_en_orden(p[i],p[i+1])
        new_p.append(l[0])
        new_p.append(l[1])
    return new_p
def operador_mutacion(p):
    new = []
    for i in range(len(p)):
        new.append(mutacion(p[i]))

    return new
def genetico(n):
    p = generar_poblacion(n)
    iter = 0
    while len(p)>=2 :
        if cant_amenazas(p[0])==0:
            print(iter)
            return p[0]
        if(len(p)==2):
            print(iter)
            return p[0]
        new_p = seleccion(p)
        new = cross_poblation(new_p)
        new2 = operador_mutacion(new)
        p = new2.copy()
        iter+=1


i = 0
count = 0
while i <30 :

    a = genetico(12)



    i+=1


