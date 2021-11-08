valor = input().split()
v1, v2, v3 = valor
v1 = int(v1)
v2 = int(v2)
v3 = int(v3)

if v1 > v2 and v1 > v3 and v2 > v3:
    print(f'{v3}\n{v2}\n{v1}\n')
elif v1 > v2 and v1 > v3 and v3 > v2:
    print(f'{v2}\n{v3}\n{v1}\n')
elif v2 > v1 and v2 > v3 and v1 > v3:
    print(f'{v3}\n{v1}\n{v2}\n')
elif v2 > v1 and v2 > v3 and v3 > v1:
    print(f'{v1}\n{v3}\n{v2}\n')
elif v3 > v1 and v3 > v2 and v2 > v1:
    print(f'{v1}\n{v2}\n{v3}\n')
elif v3 > v1 and v3 > v2 and v1 > v2:
    print(f'{v2}\n{v1}\n{v3}\n')

print(f'{v1}\n{v2}\n{v3}')