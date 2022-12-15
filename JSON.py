import json


class books():

    def __init__(self, name):
        self.name = name
        self.dane = ""

    def save_data(self):
        with open(self.name, 'w', encoding="UTF-8") as jf:
            json.dump(self.dane, jf, ensure_ascii=False, indent=2)

    def read_data(self):
        with open(self.name, 'r', encoding="UTF-8") as jf:
            text = jf.read()
        self.dane = json.loads(text)

    def collect_add_data(self):
        title = input("Podaj tytul ksiazki")
        author = input("Podaj autora ksiazki")
        price = input("Podaj cene ksiazki")

        self.dane[title] = {'title': title,
                       'author': author,
                       'price': price}
        return self.dane


    def remove_data(self):
        title = input("Podaj tytuł ksiazki, ktory chcesz usunac: ")
        del self.dane[title]

    def input_data(self):
        json_string = json.dumps(self.dane, ensure_ascii=False, indent=2).encode("UTF-8")
        print(json_string.decode())

    def data_actions(self):
        self.read_data()
        self.input_data()
        i = input("Chcesz dodac nowa ksiazke? T/N")
        if i == "Y":
            self.collect_add_data()
        else:
            i = input("Czy chcesz usunąć ksiazke ? T/N")
            if i == "Y":
                 self.remove_data()
        self.save_data()

def main():
    m = books('dane.json')
    m.data_actions()


if __name__ == '__main__':
    main()