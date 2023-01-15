import enchant
import string
import secrets
import re

znaki = ['*', '%', '£']
haslo = ""
typ_slownika = enchant.Dict("en_US")
lista_slow = []
flaga_slownika = 0

for _ in range(8):
    haslo += secrets.choice(string.ascii_lowercase)
haslo += secrets.choice(string.ascii_uppercase)
haslo += secrets.choice(string.digits)
haslo += secrets.choice(znaki)

schemat = re.compile("[a-zA-Z]+")
matche = schemat.findall(haslo)

for match in matche:
    if match.isalpha():
        lista_slow.append(match)

for slowo in lista_slow:
    if typ_slownika.check(slowo) is True:
        flaga_slownika = 1

if flaga_slownika == 0:
    print(f'Wygenerowane hasło: {haslo}')
else:
    print('Wygenerowane hasło istnieje w słowniku spróbuj ponownie.')