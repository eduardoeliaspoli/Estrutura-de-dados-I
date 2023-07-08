from Lista_encadeada import noLista
from Lista_encadeada import Lista


# Testes dos métodos insere, imprime, retira, busca, ultimo, comprimento e igual
lista1 = Lista()
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
lista4 = Lista()
lista4.insere(1)
lista4.insere(3)
lista4.insere(3)
lista4.insere(7)
print(f"Testando se é igual: {lista1.igual(lista4)}")

#Teste dos métodos insereFim, imprimeRecursivo, retiraRecursivo, igualRecursivo, libera e vazia
lista2 = Lista()
lista2.insereFim(1)
lista2.insereFim(2)
lista2.insereFim(3)
print("Antes de ser retirado: ")
lista2.imprimeRecursivo()
lista2.retiraRecursivo(3)
print("Depois de ser retirado: ")
lista2.imprimeRecursivo()
lista3 = Lista()
lista3.insereFim(1)
lista3.insereFim(2)
lista3.insereFim(3)
print(f"Testando se é igual: {lista2.igualRecursivo(lista3)}")
lista5 = Lista()
lista5.insere(1)
lista5.insere(2)
lista5.insere(3)
print(f"Libera a lista e mostra o comprimento depois de liberada: {lista5.libera()}")
print(f"Verifica se a lista é vazia: {lista5.vazia()}")


