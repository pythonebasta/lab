class AnimaleDomestico:

    def __init__(self, nome, anni):
        self.nome = nome
        self.anni = anni

    def mangia(self):
        print(self.nome, "Sta mangiando!")

    def dorme(self):
        print(self.nome, "Sta dormendo!")

class Coccodrillo(AnimaleDomestico):

    def __init__(self, nome, anni):
        super().__init__(nome, anni)

    def nuota(self):
        print(self.nome, "sta nuotando!")

class Pitone(AnimaleDomestico):

    def __init__(self, nome, anni, lunghezza):
        super().__init__(nome, anni)

    def striscia(self):
        print(self.nome, "sta strisciando!")

mio_coccodrillo = Coccodrillo("Augusto", 12)
mio_pitone = Pitone("Bob", 13, 450)

mio_coccodrillo.dorme()
mio_pitone.striscia()
