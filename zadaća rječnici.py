#zadaća
import random
imena = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

rječnik = {'1':0,'2':0,'3':0,'4':0,'5':0}
for ime in imena:
    ocjena = random.randint(1,5)
    rječnik[str(ocjena)]+= 1
print(rječnik)
print("Broj imena je", len(imena),'.')
ukupno = len(imena)
prolazi = ukupno - rječnik['1']
prolaznost = prolazi/ukupno *100
print("Prolaznost na kolokviju je",round(prolaznost,2), "%.")
