class FilaVetor: 
    def __init__(self,tam):
        self.vet = [None] * tam
        self.tam = tam
        self.n = 0
        self.ini = 0

    def enqueue(self, v):
        if self.n == self.tam:
            raise Exception("ERRO: a capacidade da fila estourou!")
        else:
            fim = (self.ini + self.n) % self.tam
            self.vet[fim] = v
            self.n += 1
    
    def __str__(self):
        elementos = [None] * self.tam
        for i in range(self.n):
            elementos[(self.ini + i) % self.tam] = self.vet[(self.ini + i) % self.tam]
        return str(elementos)
    
    def dequeue(self):
        if self.n == 0:
            raise Exception("ERRO: fila vazia!")
        else:
            v = self.vet[self.ini]
            self.ini = (self.ini + 1) % self.tam
            self.n -= 1
            return v

    def isEmpty(self):
        if self.n == 0:
            return False
        else:
            return True
        
    def reset(self):
        self.vet[0]
        self.ini = 0
        self.n = 0

    def concatena(self, f2):
        nova_fila = FilaVetor(self.tam + f2.tam)
        for i in range(self.n):
            nova_fila.enqueue(self.vet[(self.ini + i) % self.tam])
        for i in range(f2.n):
            nova_fila.enqueue(f2.vet[(f2.ini + i) % f2.tam])
        return nova_fila

    def merge(self, f2):
        nova_fila = FilaVetor(self.tam + f2.tam)
        n = min(self.n, f2.n)
        for i in range(n):
            nova_fila.enqueue(self.vet[(self.ini + i) % self.tam])
            nova_fila.enqueue(f2.vet[(f2.ini + i) % f2.tam])
        if self.n > f2.n:
            fila_resto = self
        else:
            fila_resto = f2
        for i in range(n, fila_resto.n):
            nova_fila.enqueue(fila_resto.vet[(fila_resto.ini + i) % fila_resto.tam])
        return nova_fila
    
    
fila = FilaVetor(10)
fila.enqueue(22)
fila.enqueue(23)
fila.enqueue(22)
fila.enqueue(7)
fila.dequeue()
print(str(fila))






