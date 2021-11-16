i = 1
soma = 0
while i <= 6:
    entrada = float(input())
    if entrada > 0:
        soma = soma + 1
    i = i+1
print(f'{soma} valores positivos')