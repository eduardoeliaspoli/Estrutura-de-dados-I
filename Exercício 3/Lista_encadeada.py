class noLista:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Lista:
    def __init__(self):
        self.prim = None
        self.size = 0

    def ultimo(self):
        p = self.prim
        if not self.vazia():    
            while p.prox != None:
                p = p.prox
        return p

    
    def insereFim(self, info):
        item = noLista(info) 
        if self.vazia():
            self.prim = item
        else:
            ultimo = self.ultimo()
            ultimo.prox = item

    def insere(self, info):
        novo = noLista(info)
        novo.info = info
        novo.prox = self.prim
        self.prim = novo
        self.size += 1
    
    def libera(self):
        self.prim = None


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

    def imprimeRecursivo(self):
        self.__imprimeRecursivoAux(self.prim)

    def __imprimeRecursivoAux(self, l):
        if l != None:
            print(l.info)
            self.__imprimeRecursivoAux(l.prox)
    
    def retiraRecursivo(self, v):
        self.prim = self.__retiraRecursivoAux(v, self.prim)

    def __retiraRecursivoAux(self, v, l):
        if l == None:
            return None
        elif l.info == v:
            return l.prox
        else:
            l.prox = self.__retiraRecursivoAux(v, l.prox)
        return l

    def igualRecursivo(self,l):
        return self.__igualRecursivoAux(self.prim,l.prim)

    def __igualRecursivoAux(self,l1,l2):
        if l1 == None and l2 == None:
            return True
        else:
            if l1 == None or l2 == None:
                return False
            else:
                return l1.info == l2.info and self.__igualRecursivoAux(l1.prox,l2.prox)

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
    
    def retira(self, v):    
        ant = None
        p = self.prim
        while p != None and p.info != v:
            ant = p
            p = p.prox

        if p == None:
            return
        
        if ant == None:
            self.prim = p.prox
        else:
            ant.prox = p.prox

        self.size -= 1