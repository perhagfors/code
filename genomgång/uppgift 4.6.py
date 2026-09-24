import math
bråk_tal = 1
tal=1
summa = 0
while abs(bråk_tal) > 10**-5:
    bråk_tal =(-1)**(tal-1)/tal
    summa += bråk_tal 
    tal += 1
print(f'Summan blir {summa}')
