with open('REZ1.csv', 'r') as f:
    lines = f.readlines()
    data = []
    for line in lines:
        elements = line.strip().split(';')
        ime, prezime, bodovi, naziv = elements
        print (tuple(elements))
        data.append((ime, prezime, int(bodovi), naziv))
    
        
            

    
    
    for ime, prezime, bodovi, naziv in data:
        if int(bodovi)>49:
            print(ime, prezime, " je položio/la ispit iz programiranja sa" ,bodovi, "bodova.")

data.sort(key=lambda x: x[1])
print("Sortirano po prezimenima:",data)



bodovi_rang ={
    "Nedovoljan":[],
    "Dovoljan":[],
    "Dobar":[],
    "Vrlodobar":[],
    "Izvrstan":[]
    }
for ime, prezime, bodovi, naziv in data:
    if bodovi < 50:
        bodovi_rang["Nedovoljan"].append(prezime)
    elif bodovi < 66:
        bodovi_rang["Dovoljan"].append(prezime)
    elif bodovi < 81:
        bodovi_rang["Dobar"].append(prezime)
    elif bodovi < 91:
        bodovi_rang["Vrlodobar"].append(prezime)
    else:
        bodovi_rang["Izvrstan"].append(prezime)

print(bodovi_rang)

for bodovi, studenti in bodovi_rang.items():
    print(f"{bodovi}: {len(studenti)}")
    print('\n'.join(studenti))
    
    

    
