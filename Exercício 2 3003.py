def ler_int():
    num=int(input("Digite um número inteiro:"))
    return num 

def soma_tres(num1,num2,num3):
    soma=num1+num2+num3
    return soma

x=ler_int()
y=ler_int()
z=ler_int()

resultado=soma_tres(x,y,z)

print(f"Soma dos três números: {resultado}")
