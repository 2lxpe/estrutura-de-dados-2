if __name__ == "__main__":
    temperatura = [19.9, 17.3, 24.8, 16.1, 23.0, 20.5, 15.9, 22.6, 15.6, 21.5]
    
    soma = 0
    maior = temperatura[0]
    menor = temperatura[0]
    indice_maior = 0
    indice_menor = 0
    
    for i in range(len(temperatura)):
        soma += temperatura[i]
        if temperatura[i] > maior:
            maior = temperatura[i]
            indice_maior = i
        if temperatura[i] < menor:
            menor = temperatura[i]
            indice_menor = i
            
    media = soma / len(temperatura)
    
    acima_media = 0
    for i in range(len(temperatura)):
        if temperatura[i] > media:
            acima_media += 1
            
    print("--- HANDS ON 1: TEMPERATURAS ---")
    print("Temperaturas:", temperatura)
    print(f"Média: {media:.2f} °C")
    print(f"Maior: {maior} °C (índice {indice_maior})")
    print(f"Menor: {menor} °C (índice {indice_menor})")
    print(f"Valores acima da média: {acima_media}")