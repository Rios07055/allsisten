# 1.
def facDina(n):
    cache = {} # se crea el diccionario donde se alamacenarán todos los factoriales de los números
    cache[0] = 1 # se inicializa con el fcatorial de 0 que es 1
    for i in range(1, n + 1):
        cache[i] = i * cache[i - 1]  # se recorre el diccionario hasta llegar al número ingresado, multiplicando los valores anteriores por la posción actual
    return cache[n] # se retorna el valor que se calculó 
resultado = facDina(5)
print(resultado)

# 2.
matriz = [[3, 4, 2, 10],
          [9, 1, 5, 9],
          [8, 5, 5, 8],
          [6, 3, 1, 7]]

def devolverSuma(matriz, c, c_aux, suma=0, r=0):
  if r == len(matriz)-1:
    suma += matriz[0][c]
    return suma
  if c_aux == len(matriz)-1:
    if matriz[r+1][c_aux] > matriz[r+1][c_aux-1]:
      return devolverSuma(matriz, c, c_aux, suma + matriz[r+1][c_aux], r+1)
    else:
      return devolverSuma(matriz, c, c_aux-1, suma + matriz[r+1][c_aux-1], r+1)
  if c_aux == 0:
    if matriz[r+1][c_aux] > matriz[r+1][c_aux+1]:
        return devolverSuma(matriz, c, c_aux, suma + matriz[r+1][c_aux], r+1)
    else:
      return devolverSuma(matriz, c, c_aux+1, suma + matriz[r+1][c_aux+1], r+1)
  if c_aux >= 1:
    if matriz[r+1][c_aux] > matriz[r+1][c_aux-1]:
      if matriz[r+1][c_aux] > matriz[r+1][c_aux+1]:
        return devolverSuma(matriz, c, c_aux, suma + matriz[r+1][c_aux], r+1)
      else:
        return devolverSuma(matriz, c, c_aux+1, suma + matriz[r+1][c_aux+1], r+1)
    elif matriz[r+1][c_aux-1] > matriz[r+1][c_aux+1]:
      return devolverSuma(matriz, c, c_aux-1, suma + matriz[r+1][c_aux-1], r+1)
    else:
      return devolverSuma(matriz, c, c_aux+1, suma + matriz[r+1][c_aux+1], r+1)

c = int(input("Ingresar la columna inicial: "))
suma = devolverSuma(matriz, c, c)
print(suma)

# 3.
def minDif(arr):
    n = len(arr)
    total_sum = sum(arr)
    dp = [[False for j in range(total_sum + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

    min_diff = float('inf')
    for j in range(total_sum // 2, -1, -1):
        if dp[n][j] is True:
            min_diff = total_sum - 2 * j
            break

    s1_sum = j
    s1 = []
    i = n
    while i > 0 and s1_sum > 0:
        if s1_sum - arr[i - 1] >= 0 and dp[i - 1][s1_sum - arr[i - 1]]:
            s1.append(arr[i - 1])
            s1_sum -= arr[i - 1]
        i -= 1

    s2 = [x for x in arr if x not in s1]

    return min_diff, s1, s2


arr = [11,90,22,80]
result, s1, s2 = minDif(arr)
print("diferencia mínima", result)
print(s1)
print(s2)

# 5.
def convertirString(lista):
    string = ""
    for letra in lista:
        if letra == '&# 092;&# 048;':
            break
        string += letra
    return string
 
# Función para crear cada patrón con sus espacios y posteriormente visualizarlos
def patron(string, buff, i, j, n):
    if i == n:
        bufer[j] = '&# 092;&# 048;'
        print(convertirString(bufer))
        return
    # Pone el caracter
    bufer[j] = string[i]
    patron(string, bufer, i + 1, j + 1, n)
    # Pone espacio, seguido del siguiente caracter
    bufer[j] = ' '
    bufer[j + 1] = string[i]
    patron(string, bufer, i + 1, j + 2, n)
 
# Función para guardar cada patron en buff
def imprimirPatrones(string):
    n = len(string)
    # Búfer para almacenar las combinaciones
    bufer = [0] * (2 * n)
    bufer[0] = string[0]
    patron(string, bufer, 1, 1, n)
 

string = "1234"
imprimirPatrones(string)
