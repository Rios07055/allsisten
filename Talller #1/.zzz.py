#Dado las dimensiones de una matriz de nXm, mostrar los índices de la matriz en forma de forma horizontal.

def mtr_hor(m): #O(n^2)
    cont = 0 #O(1)
    for i in range(len(m)): #O(n)
        if cont%2 != 0: #O(n)
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
___________________________________________________
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

_____________________________________

# Definición de la función para recorrer una matriz en forma de caracol
def funcion(matriz):
    vector = []  # Crear un vector para almacenar los elementos recorridos
    longitud = len(matriz)  # Obtener la longitud de la matriz (asumida cuadrada)
    direccion = 1  # Variable para controlar la dirección del recorrido
    fila, columna = longitud // 2, longitud // 2  # Inicializar fila y columna en el centro de la matriz
    contador = 0  # Contador para rastrear la cantidad de elementos recorridos

    # Realizar el recorrido hasta que se hayan recorrido todos los elementos
    while contador < longitud * longitud:
        vector.append(matriz[fila][columna])  # Agregar el elemento actual al vector
        contador += 1  # Incrementar el contador

        # Determinar la próxima dirección en la que se moverá el recorrido
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

    return vector  # Devolver el vector resultante del recorrido

# Matriz cuadrada de ejemplo
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Llamar a la función para realizar el recorrido en forma de caracol
resultado = funcion(matrix)

# Resultado esperado (comentado porque la variable no está definida en el código original)
# resultado_esperado = [5, 6, 9, 8, 7, 4, 1, 2, 3]

# Comparar el resultado obtenido con el resultado esperado
# e imprimir ambos resultados
# print(resultado == resultado_esperado)
print("Resultado del recorrido en forma de caracol:", resultado)
_______________________________________________________________________
# Definición de la función para mostrar los índices de una matriz en forma horizontal
def mtr_hor(m):
    cont = 0  # Inicializar un contador para controlar el patrón de recorrido
    for i in range(len(m)):  # Iterar a través de las filas de la matriz
        if cont % 2 != 0:  # Si el contador es impar, recorre la fila en sentido inverso
            j = 1  # Inicializar un contador inverso para recorrer la fila desde el final
            for k in range(len(m[i])):  # Iterar a través de los elementos de la fila
                print(m[i][-j], end=", ")  # Imprimir el elemento en sentido inverso
                j -= 1  # Disminuir el contador inverso para moverse hacia adelante en la fila
        else:  # Si el contador es par, recorre la fila en sentido normal
            for j in range(len(m[i])):  # Iterar a través de los elementos de la fila
                print(m[i][j], end=", ")  # Imprimir el elemento en sentido normal
        cont += 1  # Incrementar el contador para alternar entre los patrones de recorrido

# Matriz de ejemplo
m = [
    [455, 21315],
    [4, 7],
    [20, 58],
    [30, 10],
    [9, 55],
    [75, 11],
    [89, 69],
    [22, 66]
]
print("Matriz en forma horizontal:")
mtr_hor(m)  # Llamar a la función para mostrar los índices de la matriz en forma horizontal
_______________________________________________________________________
# Definición de la función para calcular la suma de dígitos pares e impares entre dos números
def suma_extremos(num1, num2, suma=0):
    # Caso base: Si ambos números llegan a ser 0, retornar la suma acumulada
    if num1 == num2 == 0:
        return suma
    else:
        # Obtener el último dígito de cada número
        mod1 = num1 % 10
        mod2 = num2 % 10

        # Si el último dígito de num1 es impar, agregarlo a la suma
        if mod1 % 2 != 0:
            suma += mod1
        # Si el último dígito de num2 es par, agregarlo a la suma
        if mod2 % 2 == 0:
            suma += mod2

        # Llamada recursiva: Eliminar el último dígito de ambos números y actualizar la suma
        return suma_extremos(num1 // 10, num2 // 10, suma)

# Números de ejemplo
num1 = 1
num2 = 5

# Llamar a la función y mostrar la suma de dígitos pares e impares entre los números
print("Números de ejemplo:", num1, "y", num2)
print("Suma de dígitos pares e impares:", suma_extremos(num1, num2))


import numpy as np
import random as rd
