valores = input().split(" ") 

cod,qutd = valores

if cod == '1':
    total = 4.00 * int(qutd)
    print('Total: R$ %.2f'%total)
elif cod == '2':
    total = 4.50 * int(qutd)
    print('Total: R$ %.2f'%total)
elif cod == '3':
    total = 5.00 * int(qutd)
    print('Total: R$ %.2f'%total)
elif cod == '4':
    total = 2.00 * int(qutd)
    print('Total: R$ %.2f'%total)
elif cod == '5':
    total = 1.50 * int(qutd)
    print('Total: R$ %.2f'%total)