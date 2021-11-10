soma = 0
n = 0
while n < 2:
    x = float(input())
    if x < 0 or x > 10:
        print('nota invalida')
    elif x >= 0 and x <= 10:
        n = n + 1
        soma = soma + x
med = soma / 2
print(f'media = {med:.2f}')
