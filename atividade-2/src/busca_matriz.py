def busca_sequencial(matriz, alvo):
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
    print("--- BUSCA SEQUENCIAL EM MATRIZES ---")
    
    dimensoes = [2, 10, 100]
    
    for dim in dimensoes:
        matriz = [[(i * dim + j + 1) for j in range(dim)] for i in range(dim)]
        total_elementos = dim * dim
        
        alvo_inicio = matriz[0][0]
        alvo_fim = matriz[dim-1][dim-1]
        alvo_inexistente = -1
        
        _, _, _, comp_inicio = busca_sequencial(matriz, alvo_inicio)
        _, _, _, comp_fim = busca_sequencial(matriz, alvo_fim)
        _, _, _, comp_inexistente = busca_sequencial(matriz, alvo_inexistente)
        
        print(f"\nMatriz {dim}x{dim} ({total_elementos} elementos):")
        print(f"  Busca no início: {comp_inicio} comparação(ões)")
        print(f"  Busca no final:  {comp_fim} comparação(ões)")
        print(f"  Inexistente:     {comp_inexistente} comparação(ões)")