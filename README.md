def string(str, cont = 0):
    if len(str) == 0:
        return cont
    else:
        return string(str[1:], cont+1)
    
print(string("123456"))
