def exibir_poltronas(lugares_onibus):
    print("Status das poltronas:")
    for i in range(50):
        if lugares_onibus[i] == 1:
            print("[X]", end=' ')
        else:
            print("[ ]", end=' ')
        if (i + 1) % 10 == 0:
            print()  # Nova linha a cada 10 poltronas
    print()

def vender_passagem(lugares_onibus):
    poltrona = int(input("Escolha uma poltrona (1-50): ")) - 1

    if poltrona < 0 or poltrona >= 50:
        print("Número de poltrona inválido!")
        return

    if lugares_onibus[poltrona] == 1:
        print("Esta poltrona já está vendida!")
    else:
        lugares_onibus[poltrona] = 1
        print("Passagem vendida com sucesso!")

def main():
    lugares_onibus = [0] * 50  # 0 = disponível, 1 = vendida
    while True:
        exibir_poltronas(lugares_onibus)
        acao = input("Deseja vender uma passagem? (s/n): ").lower()
        if acao == 's':
            vender_passagem(lugares_onibus)
        elif acao == 'n':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 