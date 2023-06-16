def generator(broj):
    for i in range(broj):
        if i %2 ==0:
            yield f"Parni broj: {i}"
        else:
            yield f"Neparni broj: {i}"
parametar = int(input("Unesite parametar"))
gen= generator(parametar)

for broj in gen:
    print(broj)
