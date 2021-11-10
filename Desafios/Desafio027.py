i = 1
soma = 0
arm = 0

while i <= 6:
    entrada = float(input())
    if entrada > 0: #se os numeros forem positivos
        soma = soma + 1  #contagem dos positivos
        arm = arm + entrada #soma dos numeros positivos
    i = i +1
media = arm/soma

print(f'{soma} valores positivos\n{media:.1f}')