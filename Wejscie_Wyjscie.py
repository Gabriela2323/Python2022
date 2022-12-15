# Zad 1

print("Hello World")

# Zad 2

print("Podaj swoje imie:")
imie = input()
print("Podaj swoje nazwisko:")
nazwisko = input()
print("Podaj roj urodzenia:")
rok = input()
lista = [imie, nazwisko, rok]
print("Twoje dane:", lista)


# Zad 3

print("Podaj kod:")
kod = input()
print("Wpisz podany wczesniej kod ponownie:")
kod2 = input()

str(kod)
str(kod2)

if kod == kod2:
    print("Kody sa takie same.")
else:
    print("Kody nie sa takie same.")


"""
#Sposób 2:
res = [x for x in l_kod + l_kod2 if x not in l_kod or x not in l_kod2]  #list comprehension
print(res)
if not res:
    print("Kod jest poprawny")
else:
    print("Kod jest niepoprawny")
    
#Sposób 3:    
import collections
if l_kod==l_kod2:
    print("Poprawny kod.")
else: print("Zly kod")
"""