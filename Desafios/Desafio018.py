hi, hf = map(int, input().split())

t = hf - hi

if t <= 0:
    t = t + 24

print(f'O JOGO DUROU {t} HORA(S)')