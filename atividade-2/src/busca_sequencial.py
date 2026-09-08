"""
Busca sequencial em matriz (loops aninhados), instrumentada.

Parte 3 da Atividade Avaliativa de Estruturas de Dados.
"""


def busca_sequencial(matriz, alvo):
    """Procura 'alvo' na matriz, linha por linha e coluna por coluna.

    Retorna (encontrado, linha, coluna, comparacoes).
    """
    linhas = len(matriz)
    colunas = len(matriz[0])
    comparacoes = 0

    for i in range(linhas):
        for j in range(colunas):
            comparacoes += 1
            if matriz[i][j] == alvo:
                return True, i, j, comparacoes

    return False, -1, -1, comparacoes


if __name__ == "__main__":
    matriz = [[i * 10 + j for j in range(10)] for i in range(10)]

    print("Busca no início:", busca_sequencial(matriz, matriz[0][0]))
    print("Busca no final:", busca_sequencial(matriz, matriz[-1][-1]))
    print("Valor inexistente:", busca_sequencial(matriz, -1))
