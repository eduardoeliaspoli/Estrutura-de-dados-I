from ArvoreBinariaBusca import NoArvoreBinaria
from ArvoreBinariaBusca import ArvoreBinaria


if __name__ == "__main__":
    arvore = ArvoreBinaria()

    arvore.insere(5)
    arvore.insere(3)
    arvore.insere(7)
    arvore.insere(2)
    arvore.insere(4)
    arvore.insere(6)
    arvore.insere(8)

    print("Árvore em ordem crescente:")
    print(arvore)

    valor_busca = 6
    resultado_busca = arvore.busca(valor_busca)
    if resultado_busca is not None:
        print(f"O valor {valor_busca} foi encontrado na árvore.")
    else:
        print(f"O valor {valor_busca} não foi encontrado na árvore.")

    valor_remover = 3
    arvore.retira(valor_remover)
    print(f"Após remover o valor {valor_remover}:")
    print(arvore)