N = 8
n = 7


def operaciones(N, valor=0, resultado=0):
  if N == valor:
    return resultado
  else:
    if valor > N:
      resultado -= 1
      valor /= 2
      return operaciones(N, valor+1, resultado + 1)
    elif valor != 0:
      return operaciones(N, valor*2, resultado + 1)
    elif valor == 0:
      return operaciones(N, valor+1, resultado + 1)



print(operaciones(N))
print(operaciones(n))
