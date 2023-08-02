def reverse(str, str2 = ""):
    if len(str) == 0:
        return str2
    else:
        new = str[-1]
        return reverse(str[:-1], str2 + new)
    

print(reverse("Camilo"))
