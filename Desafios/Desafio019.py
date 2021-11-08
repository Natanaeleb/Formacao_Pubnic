hi, mi, hf, mf = map(int, input().split())


mi = mi + hi*60
mf = mf + hf*60
minutos = mf - mi

if minutos <= 0:
    minutos = minutos + 24*60

m = minutos%60
h = minutos // 60

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')