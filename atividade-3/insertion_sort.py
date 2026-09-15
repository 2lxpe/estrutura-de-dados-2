def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0
    n = len(vetor)

    for i in range(1, n):
        chave = vetor[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1
            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        vetor[j + 1] = chave

    return comparacoes, movimentacoes
