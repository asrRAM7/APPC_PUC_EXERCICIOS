cont=cont1=cont2=cont3=cont4=0
while cont>=0:
    num=int(input("Digite um número: "))
    cont=num
    if 0>=num<=25:
        cont1+=1
    elif 26>=num<=50:
        cont2+=1
    elif 51>=num<=75:
        cont3+=1
    elif 76>=num<=100:
        cont4+=1
else:
    print(f"[0-25]={cont1} [26-50]={cont2} [51-75]={cont3} [76-100]={cont4}")