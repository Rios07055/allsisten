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
        print(horas, minutos)
        return 0
    if horas == 0:
        if minutos > 30:
            print(horas, minutos)
            return 360 - minutos*6
        else:
            print(horas, minutos)
            return minutos*6
    elif minutos == 0:
        if horas > 6:
            print(horas, minutos)
            return 360 - horas*30
        else:
            print(horas, minutos)
            return horas*30
    elif minutos > 30 or horas > 6:
        grados_1 = 360 - np.abs(minutos*6 - horas*30)
        grados_2 = np.abs(minutos*6 - horas*30)
        print(horas, minutos)
        if grados_1 > grados_2:
            return grados_2
        else:
            return grados_1
    else:
        print(horas, minutos)
        return np.abs(minutos*6 - horas*30)


print(angulo_menor(rd.randint(0, 12), rd.randint(0, 60)))
