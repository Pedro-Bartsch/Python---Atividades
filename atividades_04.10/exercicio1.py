matriz = [[0 for _ in range(10)]for _ in range(10)]

print ("Digite os valores da matriz 10x10: ")
for i in range(10):
    for j in range(10):
        matriz[i][j] = float(input(f"Campo [{i+1}][{j+1}]: "))

cont_null = 0
for linha in matriz:
    for campo in linha:
        if campo != 0:
            cont_null += 1

print (f"Número de posições não nulas na matriz: {cont_null}")