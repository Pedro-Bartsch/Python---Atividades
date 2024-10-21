def converter_quilometros_para_metros(quilometros):
    metros = quilometros * 1000 
    return metros 
try: 
    quilometros = float(input("Digite a distância em quilômetros: ")) 
    metros = converter_quilometros_para_metros(quilometros)
    print("metros:", metros) 
except ValueError: 
    print("Entrada inválida!")

#O código faz uma função que converte quilometros para metros
#Onde ele solicita o numero em quilometros e multiplica por mil para converter para metros
#E então ele faz um float(input) para gerar um prompt que leia o que foi digitado em numero real
#Por fim o código emite o valor em metros após converter de quilometros
#E caso o usuario insira um valor incorreto ele delcarará como erro.