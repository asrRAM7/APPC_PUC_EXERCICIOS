par=impar=soma_par=aux=soma_total=num=0
while num>0:
    num=float(input("Digite um número: "))
    aux+=1
    soma_total+=num
    if num%2==0:
        soma_par+=num
        par+=1
    else:
        impar+=1
print(f"Média dos pares: {soma_par/par}")
print(f"Média geral: {soma_total/aux}")