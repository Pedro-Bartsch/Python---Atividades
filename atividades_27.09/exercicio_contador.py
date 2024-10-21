contador = 0

def incrementar_contador():
    global contador
    while contador < 2:
        contador += 1
        print ("Contador atualizado: ", contador)

def exibir_contador():
    print ("Valor atual do contador atualizado: ",contador)

def adicionar_na_lista(item,lista):
    lista.append (item)
    return lista

def exibir_lista(lista):
    print ("Itens na lista: ", lista)

minha_lista = []

minha_lista = adicionar_na_lista('Maçã', minha_lista)
minha_lista = adicionar_na_lista('Banana', minha_lista)
minha_lista = adicionar_na_lista('Laranja', minha_lista)

exibir_lista(minha_lista)
incrementar_contador()
exibir_contador()