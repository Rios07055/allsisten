# 1.
def facDina(n):
    cache = {} # se crea el diccionario donde se alamacenarán todos los factoriales de los números
    cache[0] = 1 # se inicializa con el fcatorial de 0 que es 1
    for i in range(1, n + 1):
        cache[i] = i * cache[i - 1]  # se recorre el diccionario hasta llegar al número ingresado, multiplicando los valores anteriores por la posción actual
    return cache[n] # se retorna el valor que se calculó 
resultado = facDina(5)
print(resultado)
