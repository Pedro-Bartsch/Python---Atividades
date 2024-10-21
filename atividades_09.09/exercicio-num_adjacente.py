def tem_digitos_adjacentes_iguais(numeros):
    for i in range(1, len(numeros)):
        if numeros[i] == numeros[i - 1]:
            return "sim"
    return "não"

n = int(input("Digite a quantidade de números inteiros: "))

numeros = [0] * n  

for i in range(n):
    entrada = input("Digite o número " + str(i + 1) + ": ")
    numeros[i] = int(entrada)

resultado = tem_digitos_adjacentes_iguais(numeros)

print("A resposta é:", resultado)