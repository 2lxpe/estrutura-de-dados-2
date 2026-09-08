"""
Bubble Sort instrumentado (conta comparações e trocas).

Parte 2 da Atividade Avaliativa de Estruturas de Dados.
"""
import random


def bubble_sort(arr):
    """Ordena uma lista com Bubble Sort e retorna (lista_ordenada, comparacoes, trocas)."""
    a = arr.copy()
    n = len(a)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                trocas += 1
                trocou = True
        if not trocou:
            break

    return a, comparacoes, trocas


if __name__ == "__main__":
    for tamanho in (10, 20, 1000):
        dados = [random.randint(0, 10_000) for _ in range(tamanho)]
        _, comparacoes, trocas = bubble_sort(dados)
        print(f"n={tamanho:>5} | comparações={comparacoes:>7} | trocas={trocas:>7}")
