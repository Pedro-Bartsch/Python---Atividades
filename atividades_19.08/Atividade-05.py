def mdc(a, b):
    if b == 0: 
        return a 
    else: 
        return mdc(b, a % b) 
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:")) 
resultado = mdc(num1, num2)
print ("MDC:", resultado)
#O programa solicita dois numeros para fazer o mdc (maximo multiplo comum)
#O Programa faz uma condição caso se o segundo numero for igual a 0 ele retorna o primeiro numero
#O int(input) faz um prompt para que for digitado no prompt seja lido como um numero inteiro
#E então ele chama a função fazendo sua instrução
#O programa entao emite o mdc dos dois numeros digitados