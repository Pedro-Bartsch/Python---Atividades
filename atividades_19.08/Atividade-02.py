deslocamento = int(input("Digite o deslocamento: "))
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""

for letra in texto:
    if letra.isupper():
        letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)
    elif letra.islower():
        letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)
    else: letra_criptografada = letra 
    texto_criptografado += letra_criptografada
    print("Texto criptografado:", texto_criptografado)

# O código cria um prompt que faz o usuário (quem executa) digitar um número que representa o deslocamento a ser realizado no texto
# Após isso outro prompt aparecerá que é o texto a ser criptografado
# O comando for é o laço que vai se aplicará todas as letras com o comando in
# O if letra.isupper ele realiza uma ação caso as letras sejam maiusculas
# O if letra.islower ele realiza uma ação caso as letras sejam minusculas
# E então o código escreve texto criptografado, e o que o usuário digitou anteriormente. Ex.: Digitou 3 para deslocamento e letra A, o código retorna D, porque D é 3 letras após o A.
