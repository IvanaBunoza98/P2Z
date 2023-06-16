def pozdrav(ime):
    print("Pozdrav,",ime + "!")
dobrodosao = lambda ime:print("Dobrodosao,",ime+"!")
def pozovi_funkciju(ispis_dobrodoslice):
    ime = "Ivana Bunoza"
    return ispis_dobrodoslice(ime)
rezultat = pozovi_funkciju(dobrodosao)
print(rezultat)
