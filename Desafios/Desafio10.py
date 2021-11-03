nome = str(input())
salario = float(input())
vendas = float(input())

s = ((15/100)*vendas) + salario

print('TOTAL = R$ %.2f'%s,end='\n')
