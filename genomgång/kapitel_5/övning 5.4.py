konsonanter = 'bcdfghjklmnpqrstvxz'
s = input('Skriv en text: ')

ny_text = ''
for text_bokstav in s:
    bokstav = text_bokstav.lower()
    if bokstav in konsonanter:
        ny_text += bokstav + 'o' + bokstav 
    else:
        ny_text += bokstav 
print(ny_text)