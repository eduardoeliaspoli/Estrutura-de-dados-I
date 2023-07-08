from Arvore import NoArvore
from Arvore import Arvore

# Programa de teste
arvore = Arvore()

# Criação da árvore
no1 = arvore.criaNo(2)
no2 = arvore.criaNo(5)

arvore.insereFilho(no1, no2)

# Teste dos métodos
print("Árvore: ", arvore)
print("Pertence? ", arvore.pertence(5))
print("Altura: ", arvore.altura())
print("Quantidade de números pares: ", arvore.pares(arvore.raiz))
print("Quantidade de nós folha: ", arvore.folhas(arvore.raiz))

arvore2 = Arvore()
no3 = arvore2.criaNo(2)
no4 = arvore2.criaNo(5)
arvore2.insereFilho(no3, no4)

print("As árvores são iguais? ", arvore.igual(arvore.raiz, arvore2.raiz))

arvore_copia = Arvore()
arvore_copia.raiz = arvore.copia(arvore.raiz)

print("Cópia da árvore: ", arvore_copia)