comp=float(input("Digite o valor da compra:"))
pag=float(input("Digite o valor pago:"))
troco=pag-comp
cemr=troco//100
cinqr=(troco%100)//50
vinr=((troco%100)%50)//20
dezr=(((troco%100)%50)%20)//10
cincr=((((troco%100)%50)%20)%10)//5
umr=(((((troco%100)%50)%20)%10)%5)//1
print("Preço:",comp)
print("Pagamento:",pag)
print("Troco:",troco)
print("R$100:",cemr,"cédulas")
print("R$50:",cinqr,"cédulas")
print("R$20:",vinr,"cédulas")
print("R$10:",dezr,"cédulas")
print("R$1:",umr,"cédulas")