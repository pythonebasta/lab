numeri=int(input("Quanti numeri:  "))
(np,ns) = (1,1)
for i in range(numeri):
    print(np)
    (np,ns) = (ns,np+ns)
