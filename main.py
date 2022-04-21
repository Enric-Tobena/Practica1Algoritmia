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
    max_idTable = maxIdTable_iterativo(reserves)

    tables = ["FREE"] * (max_idTable + 1)
    ordered_tables = classifyValues(reserves, tables)

    return checkEmptyTables_iterativo(ordered_tables)

def maxIdTable_iterativo(reserves): 
    max_idTable = -1
    for i in range(0, len(reserves)):
        if int(reserves[i][1]) > max_idTable:
            max_idTable = int(reserves[i][1])
    
    return max_idTable
 
def classifyValues(reserves, tables):
    for i in range(0, len(reserves)):
        tables[int(reserves[i][1])] = "OCCUPIED"

    return tables

def checkEmptyTables_iterativo(ordered_tables):
    for i in range(0, len(ordered_tables)):
        if ordered_tables[i] == "FREE":
            return i
    
    return len(ordered_tables)

def bookerineManagement_recursivo(reserves):   
    max_idTable = maxIdTable_recursivo(reserves)

    tables = ["FREE"] * (max_idTable + 1)
    ordered_tables = classifyValues(reserves, tables)

    return checkEmptyTables_recursivo(ordered_tables, 0)

def maxIdTable_recursivo(reserves):
    if not reserves:
        return -1
    else:
        return max(int(reserves[0][1]), maxIdTable_recursivo(reserves[1:]))

def checkEmptyTables_recursivo(ordered_tables, idTable):
    if not ordered_tables or ordered_tables[0] == "FREE":
        return idTable
    else:
        return checkEmptyTables_recursivo(ordered_tables[1:], idTable + 1)

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

    
