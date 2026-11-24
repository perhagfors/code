n = int(input('Hur många tal?:'))
tabell = []
for i in range(0, n):
    tabell.append([])
    for j in range(0, n):
        tabell[i].append((i+1)*(j+1))
for i in range(0,n):
    for j in range(0,n):
        print(f'{tabell[i][j]:4}',end='')
    print()