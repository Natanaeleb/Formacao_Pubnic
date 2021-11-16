s = float(input())

if 0 < s <= 2000:
    print('Isento')
elif 2000.00 < s <= 3000.00:
    t8 = s - 2000.00 #até 2000 é isento, então se retira esse valor do salario total
    imp8 = (8/100)*t8  #imposto é cobrado sobre 1000, o valor que sobra, ao se retirar a prte isenta
    print(f'R$ {imp8:.2f}')
elif 3000.00 < s <= 4500.00:
    imp8 = (8/100)*1000.00 #imposto é cobrado sobre cada parte, por isso se usa a anterior
    t18 = s - 3000.00      #se divide os valores, nesse caso são retirados 3000
    imp18 = (18/100)*t18 + imp8  
    print(f'R$ {imp18:.2f}')
elif s > 4500.00:
    imp8 = (8/100)*1000.00
    imp18 = (18/100)*1500.00
    t28 = s - 4500.00
    imp28 = (28/100)*t28 + imp8 + imp18
    print(f'R$ {imp28:.2f}')