class noListaDupla:
    def __init__(self,info):
        self.info = info
        self.prox = None
        self.ant = None

class ListaDupla:
    def __init__(self):
        self.prim = None
        self.size = 0

    def insere(self, info):
        novo = noListaDupla(info)
        novo.info = info
        novo.prox = self.prim
        novo.ant = None
        if self.prim != None:
            self.prim.ant = novo
        self.prim = novo
        self.size += 1

    def imprime(self):
        p = self.prim
        while p != None:
            print(p.info)
            p = p.prox
    
    def busca(self,v):
        p = self.prim
        while p != None:
            if p.info == v:
                return p
            p = p.prox
        return None
    
    def vazia(self):
        if self.prim == None:
            return True
        else:
            return False
        
    def ultimo(self):
        p = self.prim
        if not self.vazia():    
            while p.prox != None:
                p = p.prox
        return p
    
    def insereFim(self, info):
        item = noListaDupla(info) 
        if self.vazia():
            self.prim = item
        else:
            ultimo = self.ultimo()
            ultimo.prox = item
    
    def igual(self, l):
        p1 = self.prim
        p2 = l.prim
    
        while p1 != None and p2 != None:
            p1 = p1.prox
            p2 = p2.prox
        if p1 != None or p2 != None:
            return False
   
        p1 = self.prim
        p2 = l.prim
        while p1 != None:
            if p1.info != p2.info:
                return False
            p1 = p1.prox
            p2 = p2.prox
        return True
    
    def comprimento(self):
        return self.size
    
    def libera(self):
        self.prim = None

    def retira(self, v):
        p = self.busca(v)
        while p != None:
            if p.ant == None:
                self.prim = p.prox
            else:
                p.ant.prox = p.prox
            if p.prox != None:
                p.prox.ant = p.ant
            self.size -= 1
            break  
        p = p.prox  

    def merge(self, outra_lista):
        nova_lista = ListaDupla()
        p1 = self.prim
        p2 = outra_lista.prim

        while p1 is not None and p2 is not None:
            nova_lista.insereFim(p1.info)
            nova_lista.insereFim(p2.info)
            p1 = p1.prox
            p2 = p2.prox

    
        while p1 is not None:
            nova_lista.insereFim(p1.info)
            p1 = p1.prox

    
        while p2 is not None:
            nova_lista.insereFim(p2.info)
            p2 = p2.prox

        return nova_lista


