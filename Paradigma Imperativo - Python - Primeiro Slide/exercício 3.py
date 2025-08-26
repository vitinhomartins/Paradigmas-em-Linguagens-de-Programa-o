string_array = []
for i in range(2):
    string_array.append(input("Digite uma mão: [pedra/papel/tesoura]: "))
match string_array[0]:
    case "pedra":
        match string_array[1]:
            case "tesoura":
                print("Jogador 1 ganhou!")
            case "pedra":
                print("Empate!")
            case "papel":
                print("Jogador 2 ganhou")
            case _:
                print("Entrada incorreta de dados!")
    case "papel":
            match string_array[1]:
                case "tesoura":
                    print("Jogador 2 ganhou!")
                case "pedra":
                    print("Jogador 1 ganhou!")
                case "papel":
                    print("Empate")
                case _:
                    print("Entrada incorreta de dados!")
    case "tesoura":
            match string_array[1]:
                case "tesoura":
                    print("Empate!")
                case "pedra":
                    print("Jogador 2 ganhou!")
                case "papel":
                    print("Jogador 1 ganhou!")
                case _:
                    print("Entrada incorreta de dados!")
    case _:
        print("Entrada incorreta de dados!")