from ArvoreBinaria import NoArvoreBinaria
from ArvoreBinaria import ArvoreBinaria

a = ArvoreBinaria()
b = a.insere(1,

a.insere(2,
None,
a.insere(4,None, None)
),
a.insere(3,

a.insere(5, None, None),
a.insere(6, None, None)
)
)
c = ArvoreBinaria()
d = c.insere(1,

c.insere(2,
None,
c.insere(4,None, None)
),
c.insere(3,

c.insere(5, None, None),
c.insere(7, None, None)
)
)

print(f'Pré-ordem: {a}')
print(f'Simétrica: {a.imprimeSimetrica()}')
print(f'Pós-ordem: {a.imprimePos()}')
print(f'Número de números pares: {a.pares(b)}')
print(f'Número de folhas: {a.folhas(b)}')
print(f'A árvore é vazia? {a.vazia()}')
print(f'Numero de nós: {a.numNos(b)}')
print(f'Esse número está na árvore? {a.pertence(7)}')
print(f'Altura da árvore: {a.altura(b)}')
print(f'Verifica se uma árvore é igual a outra: {a.igual(b,d)}')