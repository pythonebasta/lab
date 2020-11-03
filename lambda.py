def prodotto(x):
    return x**2

print(prodotto(3))

print()

f = lambda x: x**2
print(f(4))

print()

mio_risultato = 4 + (lambda x: x**2)(3)

print(mio_risultato)

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))
