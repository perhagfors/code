nytt_tal = 0
största_tal = 0
minsta_tal = float('inf')
while nytt_tal >= 0:
    nytt_tal = int(input('Skriv in ett tal, avsluta genom att skriva ett negativt tal:'))
    if nytt_tal > största_tal:
        största_tal = nytt_tal
    if nytt_tal < minsta_tal and nytt_tal > 0:
        minsta_tal = nytt_tal
        
print(f'Det största talet var {största_tal} och det minsta talet var {minsta_tal}.')
    