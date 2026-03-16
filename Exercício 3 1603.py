A=float(input("Digite o primeiro valor real:"))
B=float(input("Digite o segundo valor real:"))
C=float(input("Digite o terceiro valor real:"))
aux=0
if A>B:
    aux=A
    A=B
    B=aux
if A>C:
    aux=A
    A=C
    C=aux
if B>C:
    aux=B
    B=C
    C=aux
print(f"Ordem crescente:{A,B,C}")