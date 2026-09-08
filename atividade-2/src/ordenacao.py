import random
import time

def bubble_sort(arr):
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

def quick_sort(arr):
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
    tamanhos = [10, 20, 1000]
    
    print("--- EXPERIMENTO DE ORDENAÇÃO ---")
    for size in tamanhos:
        dados = [random.randint(1, 10000) for _ in range(size)]
        
        # Teste Bubble Sort
        inicio = time.time()
        _, comp_b, trocas_b = bubble_sort(dados)
        tempo_b = (time.time() - inicio) * 1000
        
        # Teste Quick Sort
        inicio = time.time()
        _, comp_q, mov_q = quick_sort(dados)
        tempo_q = (time.time() - inicio) * 1000
        
        print(f"\nTamanho: {size} elementos")
        print(f"  Bubble Sort -> Comparações: {comp_b} | Trocas: {trocas_b} | Tempo: {tempo_b:.3f} ms")
        print(f"  Quick Sort  -> Comparações: {comp_q} | Movimentações: {mov_q} | Tempo: {tempo_q:.3f} ms")