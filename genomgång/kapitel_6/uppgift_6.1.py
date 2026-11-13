antal_tal = int(input("Hur många tal vill du att den ska räkna ut?? "))
tal = [2]
k=3
for i in range(1,antal_tal):
    tal += [tal[i-1]*k]
print(tal)

