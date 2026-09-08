"""
Quick Sort instrumentado (conta comparações e movimentações).

Parte 2 da Atividade Avaliativa de Estruturas de Dados.
"""
import random


def quick_sort(arr):
    """Ordena uma lista com Quick Sort e retorna (lista_ordenada, comparacoes, movimentacoes)."""
    a = arr.copy()
    comparacoes = 0
    movimentacoes = 0

    def partition(lo, hi):
        nonlocal comparacoes, movimentacoes
        pivot = a[hi]
        i = lo - 1
        for j in range(lo, hi):
            comparacoes += 1
            if a[j] <= pivot:
                i += 1
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    movimentacoes += 1
        if i + 1 != hi:
            a[i + 1], a[hi] = a[hi], a[i + 1]
            movimentacoes += 1
        return i + 1

    def qs(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            qs(lo, p - 1)
            qs(p + 1, hi)

    qs(0, len(a) - 1)
    return a, comparacoes, movimentacoes


if __name__ == "__main__":
    for tamanho in (10, 20, 1000):
        dados = [random.randint(0, 10_000) for _ in range(tamanho)]
        _, comparacoes, movimentacoes = quick_sort(dados)
        print(f"n={tamanho:>5} | comparações={comparacoes:>7} | movimentações={movimentacoes:>7}")
