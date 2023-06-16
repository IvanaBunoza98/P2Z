def unatrag(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + unatrag(string[:-1])
unos=input('Unesite string')
result = unatrag(unos)
print(result)
