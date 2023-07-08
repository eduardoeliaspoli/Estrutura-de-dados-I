from ListaDuplamenteEncadeada import noListaDupla
from ListaDuplamenteEncadeada import ListaDupla

# Testes dos métodos insere, imprime, retira, busca, ultimo, comprimento e igual
lista1 = ListaDupla()
lista1.insere(1)
lista1.insere(3)
lista1.insere(3)
lista1.insere(7)
print("Antes de ser retirado: ")
lista1.imprime()
lista1.retira(3)
print("Depois de ser retirado: ")
lista1.imprime()
print(f"Objeto Buscado: {lista1.busca(1)}")
print(f"Ultimo objeto da lista: {lista1.ultimo().info}")
print(f"Numero de objetos na lista: {lista1.comprimento()}")
lista4 = ListaDupla()
lista4.insere(1)
lista4.insere(3)
lista4.insere(3)
lista4.insere(7)
print(f"Testando se é igual: {lista1.igual(lista4)}")

lista5 = ListaDupla()
lista5.insere(1)
lista5.insere(3)
lista5.insere(5)

lista6 = ListaDupla()
lista6.insere(2)
lista6.insere(4)
lista6.insere(6)


print("Lista1 antes da intercalação:")
lista6.imprime()

print("Lista2 antes da intercalação:")
lista6.imprime()


lista_resultante = lista5.merge(lista6)


print("Lista resultante após a intercalação:")
lista_resultante.imprime()