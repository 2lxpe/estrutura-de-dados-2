def particiona(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1
    comparacoes = 0
    trocas = 0

    for j in range(inicio, fim):
        comparacoes += 1
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
            trocas += 1

    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    trocas += 1

    return i + 1, comparacoes, trocas


def quick_sort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1

    comparacoes = 0
    trocas = 0

    if inicio < fim:
        pos_pivo, comp_part, troc_part = particiona(vetor, inicio, fim)
        comparacoes += comp_part
        trocas += troc_part

        comp_esq, troc_esq = quick_sort(vetor, inicio, pos_pivo - 1)
        comp_dir, troc_dir = quick_sort(vetor, pos_pivo + 1, fim)

        comparacoes += comp_esq + comp_dir
        trocas += troc_esq + troc_dir

    return comparacoes, trocas
