p1 = input() 
p2 = input()
p3 = input()

if p1 == 'vertebrado': #primeira classe
    if p2 == 'ave':    #segunda classe
        if p3 == 'carnivoro': #terceira classe
            print('aguia')
        elif p3 == 'onivoro':
            print('pomba')
    elif p2 == 'mamifero':
        if p3 == 'onivoro':
            print('homem')
        elif p3 == 'herbivoro':
            print('vaca')

elif p1 == 'invertebrado': #primeira classe
    if p2 == 'inseto':     #segunda classe
        if p3 == 'hematofago':  #terceira classe
            print('pulga')
        elif p3 == 'herbivoro':
            print('lagarta')
    elif p2 == 'anelideo':
        if p3 == 'hematofago':
            print('sanguessuga')
        elif p3 == 'onivoro':
            print('minhoca')




