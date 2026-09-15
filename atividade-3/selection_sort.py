def selection_sort(vetor):
    comparacoes = 0
    trocas = 0
    n = len(vetor)

    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[menor]:
                menor = j

        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            trocas += 1

    return comparacoes, trocas
