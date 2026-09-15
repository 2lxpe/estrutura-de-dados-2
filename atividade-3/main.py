import random

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort


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


def rodar_experimento(tamanhos):
    for tamanho in tamanhos:
        print(f"\nTamanho: {tamanho}")
        original = gerar_vetor(tamanho, semente=tamanho)
        testar_algoritmos(original)


if __name__ == "__main__":
    print("===== ETAPA 3: EXPERIMENTO PRINCIPAL =====")
    rodar_experimento([10, 20, 1000])
