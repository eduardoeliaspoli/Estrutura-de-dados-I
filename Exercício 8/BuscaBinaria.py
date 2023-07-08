import random

def busca(vet, elem):
    n = len(vet)
    i = 0
    while i <= n - 1:
        if elem == vet[i]:
            return i
        i += 1
    return -1

def buscaBinaria(vet, elem):
    n = len(vet)
    ini = 0
    fim = n - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if elem < vet[meio]:
            fim = meio - 1
        elif elem > vet[meio]:
            ini = meio + 1
        else:
            return meio
    return -1

def cria_vetor_embaralhado(n):
    vetor = list(range(1, n + 1))
    random.shuffle(vetor)
    return vetor
