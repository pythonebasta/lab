class Telefono:
    def __init__(self, marca, modello, colore):
        self.marca = marca
        self.modello = modello
        self.colore = colore

    def chiama(self, credito, campo):
        self.credito = credito
        if credito == True and campo == True:
            print("Sto chiamando...")
        elif credito == True and campo == False:
            print("Hai credito ma non c'è campo...")
        elif credito == False and campo == True:
            print("C'è campo ma non hai credito...")
        else:
            print("Non c'è campo e non hai credito...")

    def apri_whatsapp(self, connessione):
        self.connessione = connessione
        if connessione == True:
            print("Sto aprendo whatsapp...")
        else:
            print("Non c'è connessione ad internet...")

#istanziamo l'oggetto mio_telefono e chiamiamo i due metodi
mio_telefono = Telefono("Samsung", "s8", "bianco")
mio_telefono.chiama(True, True)
mio_telefono.apri_whatsapp(True)
