T = int(input('')) #casos de teste

for i in range(T): 
    a, b = input('').split()

    if a == b:
        R = 'De novo!'
    elif a == 'pedra':
        if b == 'lagarto' or b == 'tesoura':
            R = a
        else:
            R = b  
    elif a == 'papel':
        if b == 'pedra' or b == 'Spock':
            R = a
        else:
            R = b
    elif a == "tesoura":
        if b == "lagarto" or b == "papel":
            R = a
        else:
            R = b
    elif a == 'lagarto':
        if b == 'Spock' or b == 'papel':
            R = a
        else:
            R = b
    elif a == 'Spock':
        if b == 'tesoura' or b == 'pedra':
            R = a
        else:
            R = b
    
    if R == a:
        R = 'Bazinga!'
    elif R == b:
        R = 'Raj trapaceou!'
    t = i + 1
    print(f'Caso #{t}: {R}')
