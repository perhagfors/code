namn=[]
pris = []
while True:
    inmatning = input('Namn och pris på ett kontantkort?:')
    if inmatning == '':
        break
    inmatning = inmatning.strip()
    värden = inmatning.rpartition(' ')
    namn.append(värden[0])
    pris.append(värden[2])
billigast = min(pris)
plats = pris.index(billigast)
print(f'Villigast är {namn[plats]} med priset {billigast}')
