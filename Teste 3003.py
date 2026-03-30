def ler_int(mensagem):
    valor=int(input(mensagem))
    return valor

def somar_tres(a,b,c):
    soma=a+b+c
    return soma 

n1=ler_int("Digite o primeiro número:")
n2=ler_int("Digite o segundo número:")
n3=ler_int("Digite o terceiro número:")

resultado=somar_tres(n1,n2,n3)

print(f"Resultado:{resultado}")