antal_domare = 0
while antal_domare < 3:
    antal_domare = int(input('Hur många domare(minst 3)?:'))
poäng = 0
svårighetsgrad = 0
hopp=0
while poäng >= 0 and svårighetsgrad >= 0:
    hopp += 1
    min_poäng = 10
    max_poäng = 0
    summa_poäng = 0
    svårighetsgrad = float(input(f'Hopp {hopp}: Vilken svårighetsgrad?(skriv ett negativt tal för att avsluta):'))
    #samlar in domarpoängen
    for i in range(1,antal_domare + 1):
        domarpoäng = int(input(f'Domare {i}:s poäng:'))
        min_poäng = min(min_poäng, domarpoäng)
        max_poäng = max(max_poäng, domarpoäng)
        summa_poäng += domarpoäng
    summa_poäng = summa_poäng-max_poäng-min_poäng
    hopp_poäng = summa_poäng/(antal_domare-2)*3*svårighetsgrad
    print(f'Hoppets poäng: {hopp_poäng:.1f}')