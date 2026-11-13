inlästa_tal = input('Skriv ett godtyckligt antal tal:  ')
tal = inlästa_tal.split()
talen = [int(x) for x in tal]
count = 0
for i in range(len(talen)):
    if talen[i]< 0:
        count+= 1
print('Antal negativa tal: ', count)