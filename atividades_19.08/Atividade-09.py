def insertion_sort(lista): 
    for i in range(1, len(lista)): 
        chave = lista[i]
        j = i - 1 
    while j >= 0 and chave < lista[j]: 
        lista[j + 1] = lista[j]
        j -= 1 
        lista[j + 1] = chave 
lista=list()
i=1 
while i<=10: 
    elem = int(input("Digite um elemento da lista:"))
lista.append(elem) 
i+=1
print(lista) 
insertion_sort(lista) 
print(lista)
#Este código organiza uma lista aem ordem de inserção
#Essa lista está desenvolvida em forma de matriz por conta das abreviações j e i para linha e coluna
#A lista possui 10 elementos com o comando while e ao final do código a função é chamada e organiza a lista por ordem de inserção
#Após isso o código exibe a lista
