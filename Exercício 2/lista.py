class noLista:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Lista:
    def __init__(self):
        self.prim = None
        self.ult = None
        self.size = 0

    def insere(self, info):
        novo = noLista(info)
        novo.prox = self.prim
        self.prim = novo
        if self.ult == None:
            self.ult = novo
        self.size += 1
    
    def imprime(self):
        p = self.prim
        while p != None:
            print(p.info)
            p = p.prox

    def vazia(self):
        if self.prim == None:
            return True
        else:
            return False
    
    def busca(self, v):
        p = self.prim
        while p != None:
            if p.info == v:
                return p 
            p = p.prox
        return None

    def comprimento(self):
        return self.size
    
    def ultimo(self):
        return self.ult
    
    def retira(self, v):
        ant = None
        p = self.prim
        while p != None and  p.info < v:
            ant = p
            p = p.prox
        
        if p == None:
            return
        
        if ant == None:
            self.prim = p.prox
        else:
            ant.prox = p.prox

        self.size -= 1

novo = Lista()
novo.insere(2)
novo.insere(3)
novo.insere(4)
novo.insere(10)
novo.imprime()