from Filas import FilaVetor


fila1 = FilaVetor(3)
fila1.enqueue(1)
fila1.enqueue(2)
fila1.enqueue(3)

fila2 = FilaVetor(2)
fila2.enqueue(4)
fila2.enqueue(5)

fila_merge = fila1.merge(fila2)
print(fila_merge)

fila3 = FilaVetor(3)
fila3.enqueue(1)
fila3.enqueue(2)
fila3.enqueue(3)
fila3.dequeue()
print(fila3)

fila4 = FilaVetor(3)
fila4.enqueue(1)
fila4.enqueue(2)

fila5 = FilaVetor(2)
fila5.enqueue(3)

fila_concatenada = fila1.concatena(fila2)
print(fila_concatenada)  # [1, 2, 3]