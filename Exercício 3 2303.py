maior=seg_menor=0
for i in range(10):
    num=int(input("Digite um número: "))
    if num>maior:
        segundo_maior=maior
        maior=num
    elif num>segundo_maior:
        segundo_maior=num
print(f"MAIOR: {maior}   SEGUNDO MAIOR: {segundo_maior}")