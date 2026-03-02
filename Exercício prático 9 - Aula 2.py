num=int(input("Digite um número de três dígitos: "))
centena=int(num%10) #Pega a unidade do número lido
dezena=int((num%100)/10) #Pega a dezena do número lido
unidade=int(num/100) #Pega a centena do número lido
print("Número lido:", num)

print("Número Gerado:", centena*100+dezena*10+unidade) 
