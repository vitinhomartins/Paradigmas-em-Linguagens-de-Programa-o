n = int(input("Digite o número de jogadores a ser coletado os dados: "))
dicionarios = []
for _ in range(n):
    nome = input("Digite o nome do jogador: ")
    time = input("Digite o nome do time: ")
    posicao = input("Digite a posicao do jogador: ")
    gols = int(input("Digite o numero de gols marcados: "))
    jogador = {
        "nome" : nome,
        "time" : time,
        "posicao" : posicao,
        "gols" : gols
    }
    dicionarios.append(jogador)
    n_jogador = dicionarios[0]["nome"]
    ng_jogador = dicionarios[0]["gols"]
    for jogadores in dicionarios:
        if jogador["gols"] > ng_jogador:
            ng_jogador = jogador["gols"]
            n_jogador = jogador["nome"]
print(f"O jogador com mais gols é: {n_jogador} com {ng_jogador}!")
        
