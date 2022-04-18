# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
from random import sample, choice, shuffle

def tableGenerator(number_reserves):
    wing_types = map(lambda x: x + '-Reserva', ['JUAN', 'PEPE', 'MARIA', 'LAIA', 'MONTSE', 'PAULA'])
    L = list(wing_types)
    free_pos = sample(range(number_reserves), number_reserves >> 1)
    position = 0

    global solution
    solution = min(free_pos)

    while position <= number_reserves:
        if position not in free_pos:
            yield choice(L), str(position)
        position += 1

def reserveList (number_reserves):

    reserve_list = [i for i in tableGenerator(number_reserves * 2)]

    reserve_list = reserve_list[:number_reserves]

    shuffle(reserve_list)

    return reserve_list, solution


def bookerineManagement_iterativo(reserves):

    idTable = -1

    print (reserves)

    while len(reserves) > 0:
        left_values, right_values = classifyValues(int(reserves[0][1]), reserves)

        print("LEFT_LIST: ", left_values, len(left_values))  
        print("RIGHT_LIST: ",right_values, len(right_values)) 

        if len(left_values) + idTable == int(reserves[0][1]):
            idTable = int(reserves[0][1]) + 1  
            reserves = right_values 
            print("LEFT: ", len(left_values))
        else:
            idTable = int(reserves[0][1])    
            reserves = left_values 
            print("RIGHT: ", len(right_values))
                         

    return idTable

def classifyValues(booked_table, reserves):
    left_values = []
    right_values = []

    i = 0
    while i < len(reserves):
        print(reserves[i][1])
        if int(reserves[i][1]) < booked_table:
            left_values.append(reserves[i][1])
        else:
            right_values.append(reserves[i][1])
        
        i += 1

    return left_values, right_values

def bookerineManagement_recursivo(reserves):

    idTable = -1

    #Your code here...

    print (reserves)

    return idTable


def calcular_temps_iterativo():
    import timeit
    temps = []
    for x in range(1,200,10):
        out_reserves = reserveList(x)
        reserves = out_reserves[0]
        temps.append( (x, timeit.timeit("bookerineManagement_iterativo("+str(reserves)+")",
            setup="from __main__ import bookerineManagement_iterativo")) )
    return temps

def calcular_temps_recursivo():
    import timeit
    temps = []
    for x in range(1,200,10):
        out_reserves = reserveList(x)
        reserves = out_reserves[0]
        temps.append( (x, timeit.timeit("bookerineManagement_recursivo("+str(reserves)+")",
            setup="from __main__ import bookerineManagement_recursivo")) )
    return temps

def crear_grafica( x_list, y_list ):
    plt.scatter(x_list, y_list)
    plt.show()

def costEmpiricalComputation ():

    temps_iterativo = calcular_temps_iterativo()
    crear_grafica(*map(list, zip(*temps_iterativo)))

    temps_recursivo = calcular_temps_recursivo()
    crear_grafica(*map(list, zip(*temps_recursivo)))

    return 0

# Programa Principal para la generación de mesas y reservas dentro de un restaurante. Para ello, al programa deberemos
# de pasarle como argumentos el tamaño del restaurante en número de mesas.
if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' <list_size>')

    out_reserves = reserveList(int (sys.argv[1]))
    reserves = out_reserves [0]
    idTable = bookerineManagement_iterativo(reserves)

    costEmpiricalComputation()

    if idTable == solution:
        print ('Solucion Correcta')
    else:
        print ('Solucion Incorrecta')
