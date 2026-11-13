import math
import random


lista = [random.randint(1, 1000) for i in range(100)]
print('Det minsta talet är:', min(lista))
print('Det största talet är:', max(lista))
print('Medelvärdet är:', sum(lista)/len(lista))
