def fatorial(a):
    fator=1
    for i in range(1,a+1):
        fator=fator*i
    return fator

x=int(input("Digite o Primeiro número inteiro: "))
y=int(input("Digite o Segundo número inteiro: "))
z=int(input("Digite o Terceiro número inteiro: "))

print(f"Fatorial do Primeiro número: {fatorial(x)}")
print(f"Fatorial do Segundo número: {fatorial(y)}")
print(f"Fatorial do Terceiro número: {fatorial(z)}")