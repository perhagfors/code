total_lön = 0
dagslön = 0.01
antal_dagar = 0
while total_lön < 10**7:
    dagslön = 2**antal_dagar*0.01
    total_lön += dagslön
    antal_dagar += 1
print(f'Det tar {antal_dagar} dagar att tjäna 10 miljoner')
