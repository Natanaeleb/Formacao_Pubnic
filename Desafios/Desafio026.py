di = int(input().split()[1]) #dia inicial e transformar segunda posicao em inteiro

horario = input().split(":") #entrada e separacao das horas
hi = int(horario[0]) #hora inicial
mi = int(horario[1]) #minuto inicial
si = int(horario[2]) #segundo inicial

df = int(input().split()[1]) #dia final

horario = input().split(":")
hf = int(horario[0]) #hora final
mf = int(horario[1]) #minuto final
sf = int(horario[2]) #segundo final


min_s = 60 #minutos em segundos
hora_s = min_s * 60 #horas em segundos
dia_s = hora_s * 24 #dias em segundos

inicio = si + mi*min_s + hi*hora_s + di*dia_s #transforma valores iniciais em segundos
fim = sf + mf*min_s + hf*hora_s + df*dia_s #transforma valores finais em segundos

if inicio < fim:
    tempo = fim - inicio
    dias = int(tempo/dia_s) #segundos em dias
    tempo = tempo%dia_s   #resto para horas
    horas = int(tempo/hora_s) #horas em dias
    tempo = tempo%hora_s  #resto para minutos
    minutos = int(tempo/min_s)  #minutos em dias
    tempo = tempo%min_s  #resto para segundos
    segundos = tempo

print(f'{dias} dia(s)') 
print(f'{horas} hora(s)') 
print(f'{minutos} minuto(s)') 
print(f'{segundos} segundo(s)')    



