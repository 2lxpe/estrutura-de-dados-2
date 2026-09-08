"""
Experimento comparativo entre Bubble Sort e Quick Sort.

Gera um conjunto de dados aleatório por tamanho de array e usa a MESMA
cópia nos dois algoritmos, para garantir uma comparação justa
(reprodução do experimento da Parte 2 do trabalho).
"""
import random

from bubble_sort import bubble_sort
from quick_sort import quick_sort


def comparar(tamanhos=(10, 20, 1000), seed=None):
    if seed is not None:
        random.seed(seed)

    print(f"{'n':>6} | {'Bubble comp.':>13} | {'Bubble trocas':>13} | "
          f"{'Quick comp.':>12} | {'Quick mov.':>11}")
    print("-" * 66)

    for n in tamanhos:
        dados = [random.randint(0, 100_000) for _ in range(n)]
        _, b_comp, b_trocas = bubble_sort(dados)
        _, q_comp, q_mov = quick_sort(dados)
        print(f"{n:>6} | {b_comp:>13} | {b_trocas:>13} | {q_comp:>12} | {q_mov:>11}")


if __name__ == "__main__":
    comparar()
