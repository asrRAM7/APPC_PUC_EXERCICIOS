temp=float(input("Digite o tempo gasto na viagem em horas:"))
velo=float(input("Digite a velocidade média do automóvel em Km/h:"))
dist=velo*temp
print(f"Velocidade média: {velo} Km/h")
print(f"Tempo gasto na viagem: {temp} Horas")
print(f"Distância percorrida: {dist} Km")
print(f"Quantidade de combustível consumido: {dist/12:.2f} L")