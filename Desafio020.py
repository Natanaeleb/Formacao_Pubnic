salario = float(input())


if 0 <= salario <= 400.00:
    R = (15/100)*salario 
    NS = R + salario
    p = 15
elif 400.00 < salario <= 800.00:
    R = (12/100)*salario 
    NS = R + salario
    p = 12
elif 800.00 < salario <= 1200.00:
    R = (10/100)*salario
    NS = R + salario
    p = 10
elif 1200.00 < salario <= 2000.00:
    R = (7/100)*salario
    NS = R + salario
    p = 7
elif salario > 2000.00:
    R = (4/100)*salario
    NS = R + salario
    p = 4

print('Novo salario: {:.2f}'.format(NS))
print('Reajuste ganho: {:.2f}'.format(R))
print('Em percentual: {} %'.format(p))