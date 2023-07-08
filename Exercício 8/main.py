import time
import random
from BuscaBinaria import buscaBinaria
from BuscaBinaria import busca
from BuscaBinaria import cria_vetor_embaralhado


if __name__ == "__main__":
    tamanhos = [10**1, 10**2, 10**3, 10**4, 10**5]

    for tamanho in tamanhos:
        print(f"\nVetor com {tamanho} elementos:")
        vetor = cria_vetor_embaralhado(tamanho)
        elemento = random.randint(1, tamanho)

        start_time = time.time()
        resultado_linear = busca(vetor, elemento)
        end_time = time.time()
        tempo_gasto_linear = end_time - start_time

        vetor_ordenado = sorted(vetor)

        start_time = time.time()
        resultado_binaria = buscaBinaria(vetor_ordenado, elemento)
        end_time = time.time()
        tempo_gasto_binaria = end_time - start_time

        print("Resultado da busca linear:", resultado_linear)
        print("Tempo gasto na busca linear:", tempo_gasto_linear)
        print("Resultado da busca binária:", resultado_binaria)
        print("Tempo gasto na busca binária:", tempo_gasto_binaria)

        print("Resultado da busca linear:", resultado_linear)
        print("Tempo gasto na busca linear:", tempo_gasto_linear)
        print("Resultado da busca binária:", resultado_binaria)
        print("Tempo gasto na busca binária:", tempo_gasto_binaria)