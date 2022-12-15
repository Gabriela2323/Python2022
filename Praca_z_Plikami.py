import os
# ZAD1


def counting():
    path = r'C:\Users\ACER\Desktop\PwJP'
    count = 0
    for i in os.listdir(path):  # zwraca liste katalogow w podanej sciezce
        if os.path.isfile(os.path.join(path, i)):
            count += 1
    print('File count: ', count)


counting()

# ZAD2


def tree():
    path = r'C:\Users\ACER\Desktop\PwJP'
    p = os.listdir(path)
    print(p)  # wyswietla pliki z podanego katalogu

    def counter():
        for element in p:  # sprawdza co jest katologiem i nastepnie wypisuje jego nazwe
            if os.path.isdir(os.path.join(path, element)):
                print(element)
    counter()


tree()


# ZAD3


def conversion():
    path = r'C:\Users\ACER\Desktop\PwJP\jpg'
