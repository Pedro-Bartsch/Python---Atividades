def fatorial(n, resultado=1):
    '''
    Função que calcula o fatorial de um número inteiro n >= 0.
    Utiliza recursão para calcular o fatorial.
    '''
    if n == 0 or n == 1:  # Caso base
        return resultado
    else:  # Passo recursivo
        return fatorial(n - 1, n * resultado)

# Função principal
def main():
    n = int(input("Digite um número inteiro: "))
    resultado = fatorial(n)
    print(20 * "#")
    print("Fatorial:", resultado)
    print(20 * "#")

# Executa a função principal
if __name__ == "__main__":
    main()
#O código que o professor postou primeiramente não estava funcionando então alterei um pouco para que funcionasse corretamente**
#Esse código faz uma função que utiliza recursão de cauda para calcular um número fatorial
#Primeiramente cria-se um prompt que lê como número o que for digitado, para fazer o cálculo
#Caso o número digitado seja 1 ou 0 será retornado o número 1
#Caso normalmente digitado o número será subtraído de 1, e após isso multiplicado pelo resultado
#A função principal faz o numero fatorial do número anteriormente digitado e o exibe.
#Os print (20* "#") são apenas para decoração no qual deixa o número fatorial destacado por 20 # em cima e em baixo.