import sys
import random

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort

# o Quick Sort recursivo estoura o limite padrao de recursao do Python
# quando o vetor ja vem ordenado (pior caso), entao aumentamos o limite
sys.setrecursionlimit(5000)


def gerar_vetor(tamanho, semente):
    random.seed(semente)
    return [random.randint(1, 100000) for _ in range(tamanho)]


def testar_algoritmos(vetor_original):
    v_bubble = vetor_original.copy()
    v_insertion = vetor_original.copy()
    v_selection = vetor_original.copy()
    v_quick = vetor_original.copy()

    b_comp, b_troc = bubble_sort(v_bubble)
    i_comp, i_mov = insertion_sort(v_insertion)
    s_comp, s_troc = selection_sort(v_selection)
    q_comp, q_mov = quick_sort(v_quick)

    print(f"Bubble    -> comparacoes: {b_comp}, trocas: {b_troc}")
    print(f"Insertion -> comparacoes: {i_comp}, movimentacoes: {i_mov}")
    print(f"Selection -> comparacoes: {s_comp}, trocas: {s_troc}")
    print(f"Quick     -> comparacoes: {q_comp}, movimentacoes: {q_mov}")


def rodar_desafio(tamanho):
    base = gerar_vetor(tamanho, semente=tamanho)
    ordenado = sorted(base)
    invertido = sorted(base, reverse=True)

    casos = {
        "aleatorio": base,
        "ordenado": ordenado,
        "invertido": invertido,
    }

    for nome, vetor in casos.items():
        print(f"\n--- vetor {nome} (n={tamanho}) ---")
        testar_algoritmos(vetor)


if __name__ == "__main__":
    print("===== DESAFIO ADICIONAL =====")
    for tamanho in [10, 20, 1000]:
        rodar_desafio(tamanho)
