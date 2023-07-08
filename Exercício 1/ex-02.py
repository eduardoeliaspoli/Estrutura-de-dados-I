import random
# Função para criar vetores embaralhados
def cria_vetor_embaralhado(n):
    vetor = list(range(1, n+1))
    random.shuffle(vetor)
    return vetor
