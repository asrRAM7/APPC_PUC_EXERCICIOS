plano=int(input("Digite o seu plano de trabalho:"))
sala=float(input("Digite o seu salário:"))

match plano:
    case 1:
        print(f"Seu novo salário será: R${sala+sala*0.10:.2f}")
    case 2:
        print(f"Seu novo salário será: R${sala+sala*0.15:.2f}")
    case 3:
        print(f"Seu novo salário será: R${sala+sala*0.20:,2f}")