while True:
    try:
        texto = input()
        num_carac = len(texto)
        maiuscula = False
        minuscula = False
        num = False
        if ((num_carac > 32) or (num_carac < 6)):
            print('Senha invalida.')
        else:
            for i in range(num_carac):
                if texto[i].isupper():
                    maiuscula = True
                elif texto[i].islower():
                    minuscula = True
                elif(((ord(texto[i]))>47) and ((ord(texto[i]))<58)):
                    num = True
                else:
                    maiuscula = False
                    break
            if (maiuscula and minuscula and num):
                print('Senha valida.')
            else:
                print('Senha invalida.')
            
    except EOFError:
        break