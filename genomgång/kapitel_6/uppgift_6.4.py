inläst_lista = input('Skriv ett godtyckligt antal tal:')
lista = inläst_lista.split()
tal = [int(e) for e in lista]

while 0 in tal:
    tal.remove(0)
print(tal)

utan_nollor = [i for i in tal if tal != 0]

print(utan_nollor)