Escreva_frases = input("Digite uma string para verificar se é um palíndromo ou não: ")

Frase_corrigida = Escreva_frases.replace(" ", "").lower()
if Frase_corrigida == Frase_corrigida[::-1]:
    print ("A string é um palíndromo")
else:
    print ("A string não é um palíndromo") 