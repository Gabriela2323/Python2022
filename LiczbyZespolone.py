class LiczbaZespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im >= 0:
            return "{0} + {1}i".format(self.re, self.im)
        else:
            return "{0} {1}i".format(self.re, self.im)


    def __add__(self, z2):
        return LiczbaZespolona(self.re + z2.re, self.im + z2.im)

    def __sub__(self, z2):
        return LiczbaZespolona(self.re - z2.re, self.im - z2.im)




def main():
    x = LiczbaZespolona(2,14)
    y = LiczbaZespolona(3,5)
    z = x + y
    print(z)


if __name__ == '__main__':
    main()