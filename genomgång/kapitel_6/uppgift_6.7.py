print('Skriv en matris,rad för rad. Avsluta med tom rad.')
matris = []
count=0
while True:
    s = input('')
    if s == '':
        break
    s.replace(' ','')
    ls = s.split(',')
    rad = [float(e) for e in ls]
    matris.append(rad)
    count+=1

for i in range(0,count):
    for j in range(0,len(rad)):
        print(f'{matris[i][j]:5.1f}',end='')
    print()
    