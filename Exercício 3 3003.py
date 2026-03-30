def somaImposto(taxaImposto,custo):
    imposto_sobv=custo+(custo*(taxaImposto/100))
    return imposto_sobv

a=int(input("Digite a Taxa de Imposto em porcentagem: "))
b=int(input("Digite o Custo do Item: "))

resultado=somaImposto(a,b)
print(f"Resultado: {resultado}")