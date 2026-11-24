konsonanter = 'bcdfghjklmnpqrstvxz'
s = input('Skriv rövarspråk så översätter jag till svenska: ')
i = 0
while i < len(s):
    print(s[i], end='')
    t = s[i].lower()
    if t in konsonanter:
        i += 3
    else:
        i += 1
print(s)