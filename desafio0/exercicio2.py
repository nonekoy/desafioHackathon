pares=[]
array=[]
menorDiferenca= float("inf") #iniciei o menor no infinito para ter comparativo
num= int(input("Digite um numero, 0 para cancelar:\n"))
while num!=0:
    array.append(num)
    num= int(input("Digite um numero, 0 para cancelar:\n"))
array.sort()#para organizar a lista e ser mais rapido de passar o algoritmo
for i in range(len(array) - 1):
    diferenca = abs(array[i] - array[i + 1])
    if diferenca < menorDiferenca:  #se a diferença for menor que a existente ela sobrepõe
        menorDiferenca = diferenca  
        pares = [(array[i], array[i + 1])]
    elif diferenca == menorDiferenca:  #se a diferença for igual ela soma
        pares.append((array[i], array[i + 1])) 
print(pares)