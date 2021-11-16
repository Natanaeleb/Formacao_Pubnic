num = input().split(" ") 
n1,n2,n3,n4 = num


media = (float(n1)*2 + float(n2)*3 + float(n3)*4 + float(n4)*1)/10

if media >= 7.0:
    print('Media: %.1f\nAluno aprovado.'%media)
elif media < 5.0:
    print('Media: %.1f\nAluno reprovado.'%media)
elif 5.0 <= media < 7.0:
    print('Media: %.1f\nAluno em exame.'%media)
    nota = float(input())
    print('Nota do exame: %.1f'%nota)
    MF = (media + nota)/2
    if MF >= 5.0:
        print('Aluno aprovado.\nMedia final: %.1f'%MF)
    else:
        print('Aluno reprovado.\nMedia final: %.1f'%MF)

