linha1 = input().split() #separar as entradas
cod1,num1,val1 = linha1 #converter para inteiro

linha2 = input().split() #separar as entradas
cod2,num2,val2 = linha2

VP = (int(num1))*(float(val1)) + (int(num2))*(float(val2))

print('VALOR A PAGAR = R$ %.2f'%VP,end='\n')
