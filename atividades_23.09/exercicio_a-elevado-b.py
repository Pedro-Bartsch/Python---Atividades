a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

def elevado (a,b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado

resultado = elevado(a, b)
print (resultado)