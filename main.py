lista = [2, 3.4,"s", 4+3j]
print(lista)

lista.append(3.12)
lista.append("abc")

print(lista)

lista.insert(1,10)
print(lista)

lista.extend((2,3,4,5))
print(lista)

lista.pop(2)
print(lista)

lista.pop()
print(lista)

lista.remove(2)
print(lista)

del lista[2]
print(lista)

lista.reverse()
print(lista)

lista_nowa = [5,1.2,1,3,9,7,5.5]
lista_nowa.sort()
print(lista)