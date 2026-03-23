s=0
aux=1
for i in range(3,42,2):
    s+=aux/i
    aux+=1
print(f"O resultado é {s:.2f}")