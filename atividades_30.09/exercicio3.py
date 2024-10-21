lista1 = []
lista2 = []

for i in range(5):
    num1 = int(input("Digite o valor da primeira lista: "))
    lista1.append(num1)
    
for i in range(5):
    num2 = int(input("Digite o valor da segunda lista: "))
    lista2.append(num2)

comum = False

for num in lista1:
    if num in lista2:
        print("Números em comum:", num)
        comum = True
if not comum:
    print("Não possui números comuns")

print (lista1)
print (lista2)