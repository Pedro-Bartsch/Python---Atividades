from random import randint
opcoes = ('Pedra','Papel','Tesoura')
maquina = randint(1, 3) - 1
print ("Suas opções de jogada são : [01] PEDRA, [02] PAPEL, [03] TESOURA")
player = int(input('Qual é a sua escolha? ')) - 1

print ('A máquina jogou {}'.format(opcoes[maquina]))
print ('O player jogou {}'.format(opcoes[player]))

if maquina == 0:
    if player == 0:
        print ("Empate")
    elif player == 1:
        print ("O Player venceu")
    elif player == 2:
        print ("A máquina venceu")

elif maquina == 1:
    if player == 0:
        print ("A máquina venceu")
    elif player == 1:
        print ("Empate")
    elif player == 2:
        print ("O player venceu")

elif maquina == 2:
    if player == 0:
        print ("O player venceu")
    elif player == 1:
        print ("A máquina venceu")
    elif player == 2:
        print ("Empate")