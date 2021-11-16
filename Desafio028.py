N = int(input())
i = 1 
soma = 0

while i <= N:
    soma = soma + 2
    if soma <= N:
        q = soma*soma
        print(f'{soma}^{2} = {q}')
    i = i+1
    