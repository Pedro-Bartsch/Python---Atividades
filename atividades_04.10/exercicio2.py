from random import randint

def exibir_matriz(matriz):
    for linha in matriz:
        print(' | '.join([' ' if x == 0 else x for x in linha]))
        print('-' * 9)

def verificar_vitoria(matriz):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != 0 or \
           matriz[0][i] == matriz[1][i] == matriz[2][i] != 0:
            return True
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != 0 or \
       matriz[0][2] == matriz[1][1] == matriz[2][0] != 0:
        return True
    return False

def jogar():
    matriz = [[0] * 3 for _ in range(3)]
    vez = 'player'
    print("Jogo da velha! Você é 'x' e a máquina é 'o'.")

    for _ in range(9):
        exibir_matriz(matriz)

        if vez == 'player':
            jogada = int(input('Escolha uma posição (1-9): ')) - 1
            linha, coluna = divmod(jogada, 3)
            if 0 <= linha < 3 and 0 <= coluna < 3 and matriz[linha][coluna] == 0:
                matriz[linha][coluna] = 'x'
                vez = 'maquina'
            else:
                print("Jogada inválida! Tente novamente.")
                continue
        else:
            while True:
                linha, coluna = randint(0, 2), randint(0, 2)
                if matriz[linha][coluna] == 0:
                    matriz[linha][coluna] = 'o'
                    vez = 'player'
                    break

        if verificar_vitoria(matriz):
            exibir_matriz(matriz)
            print("Você venceu!" if vez == 'maquina' else "A máquina venceu!")
            return

    exibir_matriz(matriz)
    print("Empate!")

if __name__ == "__main__":
    jogar()