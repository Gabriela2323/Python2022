import xml.sax

class AnimalHandler(xml.sax.AnimalContent):


    def characters(self, content):
        if self.current == "gatunek":
            self.imie = content
        elif self.current == "wiek":
            self.nazwisko = content

    def endElement(self, name):
        if self.current == "gatunek":
            print(f"Gatunek: {self.imie}")
        elif self.current == "wiek":
            print(f"Wiek: {self.nazwisko}")
        self.current = ""


def main():
    handler = AnimalHandler()
    parser = xml.sax.make_parser()
    parser.setAnimalContent(handler)
    parser.parse('source.xml')


if __name__ == '__main__':
    main()

