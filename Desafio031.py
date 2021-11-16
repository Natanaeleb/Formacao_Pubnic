N = int(input()) #entrada
x = []  #lista vazia

#converte para o tipo lista(objeto map), transforma em nova lista, transforma para inteiros
numeros =list(map(int,input().split())) 
for i in range(N): #loop para inserir os numeros e pegar o menor valor
    x.append(numeros[i])
print(f'Menor valor: {min(x)}')
for i in range (N): #loop para pegar a posicao do menor valor
    if x[i] == min(x):
        posicao = i
print(f'Posicao: {posicao}')