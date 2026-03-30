def func(a,b):
    if a<b:
        menor=a
        maior=b
    else:
        menor=b
        maior=a
    for i in range(menor,maior+1):
        if i%2==0:
            print(i)

x=int(input("Digite o valor de A: "))
y=int(input("Digite o valor de B: "))

func(x,y)