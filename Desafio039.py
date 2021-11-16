n = int(input())

for nIndex in range(n): #descobrir a posicao
    letras = input().split() #lista de letras
    armazena = '' #recebe conjunto de letras ou letra

    for letra in letras: #procura os espacos na lista
        if letra != '': #espaco
            armazena += letra[0] #armazena primeira letra
    print(f'{armazena}')