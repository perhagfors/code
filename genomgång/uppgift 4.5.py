årtal=2019
while årtal <= 2019:
    årtal = int(input('Skriv ett årtal efter 2019:'))
antal_år = årtal - 2019
antal_invånare = 26000*1.001**antal_år - 25*antal_år
print(f'Det bor {round(antal_invånare)} invånare i kommunen år {årtal}.')