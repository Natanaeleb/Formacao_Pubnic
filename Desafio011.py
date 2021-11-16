linha1 = input().split(" ") 
linha2 = input().split(" ") 

cod1,num1,val1 = linha1
cod2,num2,val2 = linha2

VP = (int(num1) * float(val1)) + (int(num2) * float(val2))

print("VALOR A PAGAR: R$ %.2f"%VP)

