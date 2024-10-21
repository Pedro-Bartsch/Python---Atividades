numeros = []
for i in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida!!!")
soma = sum(numeros)
media = soma / len(numeros)
print("Soma:", soma)
print("Média:", media)
#Esse código faz um laço for que contenha 10 elementos.
#Após isso faz o comando try e except ValueError foram utilizados caso o usuário não digite um número inteiro o código exiba uma mensagem de erro.
#Então o int(input) faz com que os elementos sejam lidos como números
#O código faz a soma e a média de todos os números digitados e depois os exibe.