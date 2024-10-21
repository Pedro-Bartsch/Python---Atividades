def dobrar_lista(lista): 
    nova_lista = []
    for elemento in lista:
        novo_elemento = elemento * 2
        nova_lista.append(novo_elemento) 
    return nova_lista 
lista=list()
i=1
while i<=10: 
    elem = int(input("Digite um elemento da lista:")) 
lista.append(elem)
i+=1 
print(lista) 
nova_lista = dobrar_lista(lista)
print(nova_lista)

#Esse código pega uma lista e dobra ela, ou seja, multiplica por 2 o conteúdo da lista
#E igual o exercicio passado esse código cria uma lista vazia que possui 10 elementos com o comando while
#E no final ele chama a função dobrando a lista de tamanho e exibe a nova lista que seria a lista que foi dobrada.