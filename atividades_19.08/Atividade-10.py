def obter_ultimo_elemento(lista): 
    if lista: 
        return lista[-1]
    else: return None 
lista=list()
i=1 
while i<=5: 
    elem = int(input("Digite um elemento da lista:"))
lista.append(elem)
i+=1 
print(lista) 
ultimo_elemento = obter_ultimo_elemento(lista) 
print("Último elemento da lista:", ultimo_elemento)
#Este código faz uma função que cria uma lista 
#Essa lista possui 5 elementos por causa do comando while que é o laço de repetição
#Essa função pega o ultimo elemento da lista e o exibe para o usuário