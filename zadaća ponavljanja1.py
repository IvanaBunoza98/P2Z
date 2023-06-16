import random
import math
imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']



prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']


lista_radnika = []
for i in range (15):
           radnik = {}
           ime = random.choice(imena)
           prezime = random.choice(prezimena)
           a = round(random.uniform(4, 6), 2)
           radnik["ime"] = ime
           radnik["prezime"] = prezime
           radnik["satnica"] = a
           lista_radnika.append(radnik)



lista_radnika_touple = []
for osoba in lista_radnika:
           osoba["tjedni_sati"] = random.randint(20,30)
           isplata = round(osoba["tjedni_sati"]*osoba["satnica"],2)
           radnik = (osoba["ime"],osoba["prezime"], isplata)
           lista_radnika_touple.append(radnik)  
           

ukupna_isplata = 0
for ime,prezime,isplata in lista_radnika_touple:
            ukupna_isplata += isplata
           
print("Ukupna isplata:",round(ukupna_isplata,2))
print("Prosječna isplata:", round(ukupna_isplata/15,2))

print()
print("Radnici koji imaju isplatu iznad prosječne:")
print()
for ime, prezime, isplata in lista_radnika_touple:
           if isplata > ukupna_isplata/15:
                      print("Ime:", ime,"-", "Prezime:", prezime)
