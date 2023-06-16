import re
#zadaća1
reg ='^[iI].*[0-5]+\s[Bb]$'
unos= input('Unesite string')
podudarnost= re.match(reg, unos)
if podudarnost:
    print('Podudaranje!')
else:
    print('Nema podudaranja.')
#zadaća2
reg1 = '^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
reg2 = '^[a-z]{1}[a-zA-Z]+[0-9]*@sum\.ba$'

while 1:
    email = input("Unesi mail:")
    podudaranje = re.match(reg1, email)
    if podudaranje:
        print("Uspješan unos emaila!")
        break
    else:
        print("Pogrešan unos emaila!")

while 1:
    eduid = input("Unesi eduid:")
    match = re.match(reg2, eduid)
    if match:
        print("Uspješan unos eduid-a!")
        break
    else:
        print("Pogrešan unos eduid-a!")
        
