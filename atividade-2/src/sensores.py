"""
Hands On 2: Matriz Aplicada - Monitoramento de Sensores.

Matriz 5 x 24 (5 sensores x 24 medições/hora): calcula médias por
sensor, maior temperatura registrada (com sensor e horário), média
geral e quantidade de leituras acima de um limite informado.

Parte 5 da Atividade Avaliativa de Estruturas de Dados.
"""
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
    sensores = [[round(random.uniform(15.0, 30.0), 1) for _ in range(24)] for _ in range(5)]

    media_sensor, maior_temp, sensor_maior, horario_maior, media_geral, acima_limite = (
        analisar_sensores(sensores, limite=28.0)
    )

    for i, m in enumerate(media_sensor):
        print(f"Sensor {i}: média {m:.2f} °C")
    print(f"Maior temperatura: {maior_temp} °C (Sensor {sensor_maior}, {horario_maior}h)")
    print(f"Média geral: {media_geral:.2f} °C")
    print(f"Leituras acima de 28.0 °C: {acima_limite}")
