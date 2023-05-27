def asterisco(numero):#função que retorna a lista
    lista=[]
    i = 0
    while i<numero:
        lista.append('*'*i+1)
        i+=1
    return lista

lista=[]
num = int(input("Digite um numero:"))
lista = asterisco(num)
print(lista)