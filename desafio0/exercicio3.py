def subconjuntos(numeros): #função a fim de definir os subconjuntos existentes no conjunto a ser atribuido
    subconjuntos=[[]]#esse conjunto ja vem com o subconjunto vazio como padrão
    for numero in numeros:
        novoSubconjuntos=[]
        for subconjunto in subconjuntos:#aqui ele checa quantos subconjuntos posso formar com o numero retirado do conjunto
            subconjuntoAUX = subconjunto+[numero]
            novoSubconjuntos.append(subconjuntoAUX)
        subconjuntos.extend(novoSubconjuntos)#adicionando todos os subconjuntos ao meu array de subconjuntos
    return subconjuntos

numeros = []
num = int(input("digite um numero, 0 para cancelar\n"))
while num != 0:
    numeros.append(num)
    num = int(input("digite um numero, 0 para cancelar\n"))

subconjunto = subconjuntos(numeros)
print(subconjunto)
