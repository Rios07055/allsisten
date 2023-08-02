def string(str, cont = 0):
    if len(str) == 0:
        return cont
    else:
        return string(str[1:], cont+1)
    
print(string("123456"))



def reverse(str, str2 = ""):
    if len(str) == 0:
        return str2
    else:
        new = str[-1]
        print(new)
        return reverse(str[:-1], str2 + new)
    

print(reverse("JuanDavid"))
