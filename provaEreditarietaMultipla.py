class madre:
    def __init__(self):
        pass

    def parla(self):
        print("Parla la classe madre")

class figlia(madre):
    def __init__(self): 
        pass

    #def parla(self): 
        #print("Parla la classe figlia")

class figlio(madre):
    def __init__(self): 
        pass

    def parla(self): 
        print("Parla la classe figlio")

class nipote(figlia, madre):
    def __init__(self): 
        pass

   #def parla(self):
    #   print("Parla la classe nipote")

mia_classe = nipote()
print()
mia_classe.parla()
print()
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

