def corrida_tempos(tempos):
    for i, piloto in enumerate(tempos, start=1):
        print(f"Piloto {i}: " + ', '.join(f"{tempo:.2f} s" for tempo in piloto))
        print(f"Média: {sum(piloto) / len(piloto):.2f} s\n")

def main():
    tempos = [[float(input(f"Piloto {i+1}, Volta {j+1}: ")) for j in range(4)] for i in range(4)]
    corrida_tempos(tempos)

if __name__ == "__main__":
    main()