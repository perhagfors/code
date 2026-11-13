import datetime
person_nr = input('Skriv ditt personnummer som ååmmddnnnn: ')
datum = datetime.datetime.now()
s = str(datum.date())
if person_nr[2:4] == s[5:7] and person_nr[4:6] == s[8:]:
    print('Grattis!')
