antal_rader = int(input('Antal rader?:'))
for rad in range(1,antal_rader+1):
    for kolumn in range(1,11):
        print(f'{rad*kolumn:4}', end='')
    print('')
