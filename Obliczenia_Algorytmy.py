import math
import random


# ZAD1


def rownanie():
    print(" Podaj wspolczynniki rownania kwadratowego")
    a = int(input(" Wprowadz liczbe a: "))
    b = int(input(" Wprowadz liczbe b: "))
    c = int(input(" Wprowadz liczbe c: "))
    print(type(a))
    delta = b*b-4*a*c
    if delta > 0:
        print("Rownanie ma dwa rozwiazania ")
        x1 = (b - math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(" x1= ", x1, "x2 = ", x2)
    elif delta == 0:
        print("Rownanie ma jedno rozwiazanie")
        x0 = -b/2*a
        print(" x0 = ", x0)
    else:
        print("Rownanie nie ma rozwiazan")

# ZAD2


def sort():
    lista = []
    for i in range(5):
        n = random.randint(0, 100)
        lista.append(n)
    print("Random numbers: ", lista)
    size_list=len(lista)
    print (size_list)
    for i in range(size_list):
        for j in range(size_list-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(lista)

# ZAD3


def vector():

    v1 = [1, 2, 12, 4]
    v2 = [2, 4, 2, 8]
    wynik_koncowy = suma(v1, v2)
    print('Wynik iloczynu skalarnegp: ', wynik_koncowy)


def suma(v1, v2):
    scalar_list = []
    v1_size = len(v1)
    v2_size = len(v2)
    if v1_size != v2_size:
        print("Nie mozna obliczyc iloczynu skalarnego")
    if v1_size == v2_size:
        for i in range(v1_size):
            multiplication = v1[i] * v2[i]
            scalar_list.append(multiplication)
    wynik = sum(scalar_list)
    return wynik
vector()

# Zad 4
import numpy as np
from numpy import random


def matrix():
    m1 = random.randint(1001, size=(128, 128))
    m2 = random.randint(1001, size=(128, 128))
    # sprawdzenie pierwszych liczb z macierzy
    print(m1[0, 0])
    print(m2[0, 0])
    wynik_koncowy = sum_m(m1, m2)
    print("Wynik sumowania macierzy to:\n ", wynik_koncowy)


def sum_m(m1, m2):
  #  m3 = np.zeros((128, 128))
  #  for i in range(128):
  #      for j in range(128):
  #          m3[i][j] = m1[i][j] + m1[i][j]
    result = m1+m2
    return result


# Zad 5
def multiply():
    m1 = random.randint(0, 50, size=(8, 8))
    m2 = random.randint(0, 50, size=(8, 8))
    # sprawdzenie pierwszych liczb z macierzy
    print(m1[0, 0])
    print(m2[0, 0])
    print('m1*m2 = ', np.multiply(m1,m2))

# ZAD 6


def matrix_det():
    m1 = random.randint(0, 8, size=(8, 8))
    print('Macierz m1: \n', m1, '\n')
    wyznacznik_koncowy = det(m1)
    print ( "Wyznacznik  wynosi: ", wyznacznik_koncowy)


def det(m1):
    wyznacznik = abs(np.linalg.det(m1))
    return wyznacznik


if __name__ == '__main__':
    matrix_det()
