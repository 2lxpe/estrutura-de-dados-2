import random

def analisar_sensores(sensores, limite):
    n_sensores = len(sensores)
    n_horas = len(sensores[0])
    
    media_sensor = [0.0] * n_sensores
    soma_geral = 0.0
    maior_temp = sensores[0][0]
    sensor_maior = 0
    horario_maior = 0
    acima_limite = 0
    
    for i in range(n_sensores):
        soma_sensor = 0.0
        for j in range(n_horas):
            temp = sensores[i][j]
            soma_sensor += temp
            soma_geral += temp
            
            if temp > maior_temp:
                maior_temp = temp
                sensor_maior = i
                horario_maior = j
                
            if temp > limite:
                acima_limite += 1
                
        media_sensor[i] = soma_sensor / n_horas
        
    media_geral = soma_geral / (n_sensores * n_horas)
    return media_sensor, maior_temp, sensor_maior, horario_maior, media_geral, acima_limite

if __name__ == "__main__":
    random.seed(42)
    sensores = [[round(random.uniform(18.0, 30.0), 2) for _ in range(24)] for _ in range(5)]
    limite = 28.0
    
    medias, maior_t, s_maior, h_maior, m_geral, acima_lim = analisar_sensores(sensores, limite)
    
    print("--- HANDS ON 2: MONITORAMENTO DE SENSORES ---")
    for idx, m in enumerate(medias):
        print(f"Sensor {idx}: Média = {m:.2f} °C")
        
    print(f"\nMaior temperatura registrada: {maior_t:.2f} °C")
    print(f"Sensor responsável: Sensor {s_maior}")
    print(f"Horário da ocorrência: {h_maior}h")
    print(f"Média geral (120 medições): {m_geral:.2f} °C")
    print(f"Leituras acima de {limite} °C: {acima_lim}")