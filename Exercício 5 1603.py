x=float(input("Digite o valor de x:"))
n=int(input("Digite um valor inteiro não negativo:"))
contador=0
aux=1
while contador < n:
    aux=aux*x
    contador=contador+1
print(f"Resultado:{aux}")