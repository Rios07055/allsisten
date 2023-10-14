N = 8
n = 7


def operaciones(N, valor=0, resultado=0):
  if N == valor:
    return resultado
  elif N%2 == 0:
    if valor == 0:
      return operaciones(N, valor+1, resultado + 1)
    elif N == valor*2:
      return operaciones(N, valor*2, resultado + 1)
    elif N - valor > valor*2:
      return operaciones(N, valor*2, resultado + 1)
    else:
      return operaciones(N, valor+1, resultado + 1)
  else:
    if valor == 0:
      return operaciones(N, valor+1, resultado + 1)
    elif N-1 == valor*2:
      return operaciones(N, valor*2, resultado + 1)
    elif (N-1) - valor > valor*2:
      return operaciones(N, valor*2, resultado + 1)
    else:
      return operaciones(N, valor+1, resultado + 1)


print(operaciones(N))
print(operaciones(n))
