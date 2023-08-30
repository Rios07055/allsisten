#Dado las dimensiones de una matriz de nXm, mostrar los índices de la matriz en forma de forma horizontal.

def mtr_hor(m): #O(n^2)
    cont = 0 #O(1)
    for i in range(len(m)): #O(n)
        if cont % 2 != 0: #O(n)
            j = 1 #O(n)
            for k in range(len(m[i])): #O(n^2) 
                print(m[i][-j], end=", ") #O(n^2)
                j -= 1 #O(n^2)
        else: #O(n)
            for j in range(len(m[i])): #O(n^2)
                print(m[i][j], end=", ") #O(n^2)
        cont += 1 #O(n)



m = [[455,21315], 
     [4,7],
     [20,58],
     [30, 10],
     [9,55],
     [75, 11],
     [89,69],
     [22,66]] #O(1)
print(mtr_hor(m)) #O(n^2)

# Calcule la suma de los números impares por un lado y los números pares por otro entre dos números enteros
# dados (suponga que el primero es menor que el segundo, e incluya los números extremos en la suma).

def suma_extremos(num1, num2, suma = 0):
    if num1 == num2 == 0:
        return suma
    else:
        mod1 = num1 % 10
        mod2 = num2 % 10
        if mod1 % 2 != 0:
            suma += mod1
        if mod2 % 2 == 0:
            suma += mod2
        return suma_extremos(num1//10, num2//10, suma)
    
num1 = 14678
num2 = 52579
print(suma_extremos(num1, num2))


import numpy as np
import random as rd


# Dado dos enteros que indican la hora y los minutos muestre el ángulo
# menor entre las dos manecillas de un reloj análogo.
def angulo_menor(horas: int, minutos: int) -> int:
    if horas*5 == minutos:
        return 0
    if horas == 0:
        if minutos > 30:
            return 360 - minutos*6
        else:
            return minutos*6
    elif minutos == 0:
        if horas > 6:
            return 360 - horas*30
        else:
            return horas*30
    elif minutos > 30 or horas > 6:
        grados_1 = 360 - np.abs(minutos*6 - horas*30)
        grados_2 = np.abs(minutos*6 - horas*30)
        if grados_1 > grados_2:
            return grados_2
        else:
            return grados_1
    else:
        return np.abs(minutos*6 - horas*30)


print(angulo_menor(rd.randint(0, 12), rd.randint(0, 60)))

# Reorganización del código anterior.
import numpy as np


def angulo_menor(horas: int, minutos: int) -> int:
    # Condición simple
    if horas*5 == minutos:
        return 0
    # Medimos los ángulos de dos formas diferentes
    # Éste mide el ángulo que se forma por la exterior de las manecillas
    angulo_1 = 360 - np.abs(horas*30 - minutos*6)
    # Éste mide el ángulo que se forma por la interior de las manecillas
    angulo_2 = np.abs(horas*30 - minutos*6)
    # Compara ambos ángulos para ver cuál es el menor y lo retorna
    if angulo_2 > angulo_1:
        return angulo_1
    else:
        return angulo_2


print(angulo_menor(12, 15))


# Reorganización del ejercicio anterior usando recursión.
def angulo_menor(horas: int, minutos: int, grados=0) -> int:
    # Caso base
    if horas*5 == minutos:
        # Toma el ángulo exterior
        if grados > 180:
            grados = 360 - grados
            return grados
        # Toma el ángulo interior
        else:
            return grados
    # Comparamos cuál es mayor para luego "igualar" las manecillas mediante la recursión
    elif horas*5 > minutos:
        # Cada minuto sumado representa 6 grados en el reloj
        return angulo_menor(horas, minutos + 1, grados + 6)
    else:
        # Cada hora sumada representa 30 grados en el reloj
        return angulo_menor(horas + 1, minutos, grados + 30)


print(angulo_menor(3, 55))




# • Dado la dimensión de una matriz cuadrada muestre los valores en
# forma de caracol o vórtice.
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
# Valor Esperado = [5,6,9,8,7,4,1,2,3]

def funcion(matriz):
    vector = []
    longitud = len(matriz)
    direccion = 1
    fila, columna = longitud // 2, longitud // 2
    contador = 0
    
    while contador < longitud * longitud:
        vector.append(matriz[fila][columna])
        contador += 1
        
        if direccion == 0:  # centro
            direccion = 1
            columna += 1
        elif direccion == 1:  # derecha
            if columna == longitud - 1:
                direccion = 4
                fila += 1
            else:
                columna += 1
        elif direccion == 4:  # abajo
            if fila == longitud - 1:
                direccion = 3
                columna -= 1
            else:
                fila += 1
        elif direccion == 3:  # izquierda
            if columna == 0:
                direccion = 2
                fila -= 1
            else:
                columna -= 1
        elif direccion == 2:  # arriba
            if fila == 0:
                direccion = 1
                columna += 1
            else:
                fila -= 1
                
    return vector

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado_esperado = [5, 6, 9, 8, 7, 4, 1, 2, 3]
resultado = funcion(matrix)
print(resultado == resultado_esperado)
print(resultado)
