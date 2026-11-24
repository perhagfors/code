n = int(input('Tabellens storlek?:'))
tabell = []

for i in range(0,n):
    tabell.append([])
    for j in range(0,i+1):
        tabell[i].append((i+1)*(j+1))
