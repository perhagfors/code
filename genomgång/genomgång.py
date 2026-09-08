Mätarstälning_idag = int(input('Mätarstälning i dag?:'))
Mätarstälning_ett_år_sen = int(input('Mätarstälning för ett år sedan?:'))
total_mil = (Mätarstälning_ett_år_sen + Mätarstälning_idag)/10
förbrukning = 0.83

print(f'Antal körda mil: {total_mil}')
print(f'Antal liter bensin: {total_mil * förbrukning}')
print(f'Förbrukning per mil: {förbrukning}')