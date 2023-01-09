def problema_das_n_rainhas(N, tabuleiro, linha):
    # se chegarmos a ultima linha, retornamos verdadeiro
    if linha == N:
        return True
    # tente colocar uma rainha em cada coluna da linha atual
    for coluna in range(N):
        # verifique se a posição é segura para a rainha
        if ta_seguro(tabuleiro, linha, coluna):
            # coloque a rainha na posição e tente resolver o resto do tabuleiro
            tabuleiro[linha][coluna] = 1
            if problema_das_n_rainhas(N, tabuleiro, linha + 1):
                return True
            # se não conseguir resolver, remova a rainha e tente a próxima posição
            tabuleiro[linha][coluna] = 0
    # se não conseguir colocar a rainha em nenhuma posição, retorne falso
    return False

def ta_seguro(tabuleiro, linha, coluna):
    # verifique se a coluna está livre
    for i in range(linha):
        if tabuleiro[i][coluna] == 1:
            return False
    # verifique se a diagonal principal está livre
    i = linha - 1
    j = coluna - 1
    while i >= 0 and j >= 0:
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # verifique se a diagonal secundária está livre
    i = linha - 1
    j = coluna + 1
    while i >= 0 and j < len(tabuleiro):
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j += 1
    # se não houver problemas, retorne verdadeiro
    return True

# teste o algoritmo
N = 4
tabuleiro = [[0 for _ in range(N)] for _ in range(N)]
if problema_das_n_rainhas(N, tabuleiro, 0):
    for linha in tabuleiro:
        print(linha)
else:
    print("Não é possível colocar as rainhas no tabuleiro.")