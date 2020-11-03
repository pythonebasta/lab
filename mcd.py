primo_numero=int(input('Inserisci il primo numero: '))
secondo_numero=int(input('Inserisci il secondo numero: '))

while secondo_numero>0:
    resto=primo_numero%secondo_numero
    primo_numero,secondo_numero=secondo_numero,resto

print("il MCD tra i due numeri è: ",primo_numero)
