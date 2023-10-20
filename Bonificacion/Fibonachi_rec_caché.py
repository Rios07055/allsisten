#Caché
def ficboCache(n, cache = []):
  if len(cache) >= n:
    return cache[n-1]
  if n <= 1:
    cache.append(0)
    cache.append(n)
    return n
  else:
    suma = ficboCache(n - 1, cache) + ficboCache(n - 2, cache)
    cache.append(suma)
    return suma
      
ficboCache(100)
