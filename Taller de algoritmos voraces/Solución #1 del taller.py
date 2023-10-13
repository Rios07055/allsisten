a = [3, 1, 1]
b = [6, 5, 4]
c = [6, 1, 9, 5, 4]
d = [3, 4, 8, 2, 4]
def quitar_valor(c, valor):
  for j in range(len(c)):
    if c[j] == valor:
      c.pop(j)
      return valor, c

def implementacion(a: list, b: list):
  if len(a) == len(b):
    suma_a = 0
    suma_b = 0
    for j in a:
      suma_a += j
    for j in b:
      suma_b += j
    if suma_a > suma_b:
      resultado = 0
      for j in range(len(b)):
        x, b = quitar_valor(b, min(b))
        y, a = quitar_valor(a, max(a))
        resultado += x*y
    else:
      resultado = 0
      for j in range(len(b)):
        x, a = quitar_valor(a, min(a))
        y, b = quitar_valor(b, max(b))
        resultado += x*y
    return resultado
  else:
    return "Las listas no tienen igual longitud"

print(implementacion(a, b))
print(implementacion(c, d))

