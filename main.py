# -*- coding: utf-8 -*-

import re
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

    if len(reserves) > 0:
        ordered_tables = classifyValues(reserves)      
        for i in range (0, len(ordered_tables)):
            idTable = i
            if idTable != ordered_tables[i]:
                return idTable            
        
        return idTable + 1

    return idTable


def classifyValues(reserves):
    ordered_tables = []

    for i in range(0, len(reserves)):   
        ordered_tables.append(int(reserves[i][1]))        
        i += 1

    ordered_tables.sort()
    return ordered_tables
    

def bookerineManagement_recursivo(reserves):
    ordered_tables = classifyValues(reserves)
    return checkEmptyTables(ordered_tables, 0)
    

def checkEmptyTables(ordered_tables, idTable):
    if not ordered_tables or idTable != ordered_tables[0]:
        return idTable
    else:
        return checkEmptyTables(ordered_tables[1:], idTable + 1)


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
