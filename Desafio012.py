
val = int(input())
print(val)
n1 = val // 100
val = val - n1*100

n2 = val // 50
val = val - n2*50

n3 = val // 20
val = val - n3*20

n4 = val // 10
val = val - n4*10

n5 = val // 5
val = val - n5*5

n6 = val // 2
val = val - n6*2

n7 = val // 1
val = val - n1*1

print('%i nota(s) de R$ 100,00'%n1)
print('%i nota(s) de R$ 50,00'%n2)
print('%i nota(s) de R$ 20,00'%n3)
print('%i nota(s) de R$ 10,00'%n4)
print('%i nota(s) de R$ 5,00'%n5)
print('%i nota(s) de R$ 2,00'%n6)
print('%i nota(s) de R$ 1,00'%n7)
