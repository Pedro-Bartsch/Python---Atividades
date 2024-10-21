def maior_menor(lista):
    maior = lista[0]
    menor = lista[0] 
    for elemento in lista:
        if elemento > maior:
            maior = elemento
        elif elemento < menor:
            menor = elemento
    return maior, menor

lista=list()
i=1 
while i<=10: 
    elem = int(input("Digite um elemento da lista:")) 
lista.append(elem)
i+=1
print(lista) 
maior, menor = maior_menor(lista) 
print("Maior:", maior) 
print("Menor:", menor)

#A função declara uma lista com as condições se o menor elemento dessa lista for menor que a variavel menor ela recebe o valor menor
#Outra condição se o maior elemento dessa lista for maioror que a variavel maior ela recebe o valor maior
#E essa lista esta em forma de vetor
#O while acrescenta 10 elementos a lista
#Então o prompt le os elementos como numeros por conta do int(input)
#Então o programa escreve a lista e mostra o maior e menor numero dessa lista