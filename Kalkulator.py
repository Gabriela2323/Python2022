from liczbyzespolone import LiczbaZespolona


def Read_data():
    liczba1 = input("Podaj 1 liczbe zespolona: ")
    znak = input("Wybierz dzialanie jakie chcesz wykonac:")
    liczba2 = input("Podaj 2 liczbe zespolona: ")
    return [liczba1, liczba2, znak]


def complex_to_number(sign: str):
    tmp = sign.split("+")
    if len(tmp) == 1:   #check sign of imaginary part
        tmp = sign.split("-")
        im = int(tmp[1].replace("i", "")) * (-1)
    else:
        im = int(tmp[1].replace("i", ""))
    re = int(tmp[0])
    return LiczbaZespolona(re, im)

def calculator(rownanie: list):

    x = complex_to_number(rownanie[0])
    y = complex_to_number(rownanie[1])
    znak = rownanie[2]

    match znak:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y


def main():
    print(calculator(Read_data()))


if __name__ == '__main__':
    main()