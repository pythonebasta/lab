mestieri=('Medico', 'Informatico', 'Operaio', 'Industriale', 'Commercialista', 'Falegname')
redditi=[]

n=len(mestieri) #ottengo la lunghezza della tupla

for i in range(n):
    v=int(input('Reddito mensile di un ' + mestieri[i] + ': '))

    while v<1 or v>10000000:
        v=int(input('Reddito mensile di un ' + mestieri[i] + ': '))

    redditi.append(v)

s=0
massimo=redditi[0]
minimo=redditi[0]

for i in range(n):
    print('Il reddito del ', mestieri[i], 'è', redditi[i])
    s+=redditi[i]
    if redditi[i]>massimo:
        massimo=redditi[i]
    elif redditi[i]<minimo:
        minimo=redditi[i]

print('La media è', s/len(redditi))

j = redditi.index(minimo)
print('Il reddito più basso è quello pari ad euro:', minimo, 'di un ', mestieri[j])

j = redditi.index(massimo)
print('Il reddito più alto è quello pari ad euro:' , massimo, 'di un ', mestieri[j])
