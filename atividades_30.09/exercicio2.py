notas = []

n = int(input("Entre com o número de notas: "))
for i in range(n):
    dado = float(input("Entre com a nota " + str(i+1) + ": "))
    notas.append(dado)
    media = sum(notas)/n
print("As notas digitadas são: ",notas)
print("A média das notas digitadas é : ",media)