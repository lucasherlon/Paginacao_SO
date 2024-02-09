from itertools import cycle

swap = []
memoria = []
tabela_paginas = [
    ["111", 0],
    ["010", 0],
    ["110", 0],
    ["000", 0],
    ["001", 0],
    ["011", 0],
    ["100", 0],
    ["101", 0],
    ["111", 0],
    ["010", 0],
    ["110", 0],
    ["000", 0],
    ["001", 0],
    ["011", 0],
    ["100", 0],
    ["101", 0]
]

paginas = [
    "0000010101010100101",
    "0001010101010100101",
    "0010010101010100101",
    "0011010101010100101",
    "0100010101010100101",
    "0101010101010100101",
    "0110010101010100101",
    "0111010101010100101",
    "1000010101010100101",

    "1100010101010100101",
    "1101010101010100101",
    "1110010101010100101",
    "1111010101010111111",
]

def tranforma_bits_inteiro(bits):
    return int(bits, 2)
    
def escalonador(logico):
    posi = tranforma_bits_inteiro(logico[:4])
    pg = tabela_paginas[posi][0]
    for i in range(len(tabela_paginas)):
        if tabela_paginas[i][0] == pg and tabela_paginas[i][1] == 1 and posi != i:
            tabela_paginas[i][1] = 0
            for i in range(len(swap)):
                if swap[i][:3] == pg:
                    swap.remove(swap[i])
                    break
            for i in range(len(memoria)):
                if memoria[i][:3] == pg:
                    swap.append(memoria[i])
                    memoria.remove(memoria[i])
                    break
            break
    tabela_paginas[posi][1] = 1
    fisico = tabela_paginas[posi][0]+logico[4:]
    memoria.append(fisico)
    print(f'Pagina {logico[:4]} foi para a memoria')

def remover_processo(logico):
    posi = tranforma_bits_inteiro(logico[:4])
    end = tabela_paginas[posi][0] + logico[4:]
    find = False
    for i in range(len(memoria)):
        if memoria[i] == end:
            memoria.remove(memoria[i])
            find = True
            break
    if find == False:
        print("Processo não encontrado")
    else:
        print("Processo removido")
        tabela_paginas[posi][1] = 0
        volta = ""
        for i in range(len(swap)):
            if swap[i][:3] == end[:3]:
                volta = swap[i]
                memoria.append(swap[i])
                swap.remove(swap[i])
                for j in range(len(tabela_paginas)):
                    if tabela_paginas[j][0] == volta[:3] and posi != j:
                        tabela_paginas[j][1] = 1
                        print("Processo encontrado na memoria")
                        break
# Testes
print(escalonador(paginas[7]))
print(escalonador(paginas[-1]))
print(f"Memoria {memoria}")
print(f"Swap {swap}")
print(tabela_paginas[7])
print(tabela_paginas[-1])
print(escalonador(paginas[7]))
print(f"Memoria {memoria}")
print(f"Swap {swap}")
print(tabela_paginas[7])
print(tabela_paginas[-1])
"""remover_processo(paginas[-1])
print(f"Memoria {memoria}")
print(f"Swap {swap}")
print(tabela_paginas[7])
print(tabela_paginas[-1])"""

