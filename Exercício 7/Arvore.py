class NoArvore:
    def __init__(self, info: int):
        self.info = info
        self.prim = None
        self.prox = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def criaNo(self, info):
        novo = NoArvore(info)
        self.raiz = novo
        return novo
    
    def insereFilho(self, pai, filho):
        s = ''
        filho.prox = pai.prim
        pai.prim = filho
        self.raiz = pai


    def __str__(self):
        return self.__imprimeAux(self.raiz)
    
    def __imprimeAux(self,no):
        s = ''
        s = s + '<'
        s = s + str(no.info)
        p = no.prim
        while p != None:
            s = s + self.__imprimeAux(p)
            p = p.prox
        s = s + '>'
        return s
    
    def pertence(self, v):
        return self.__pertence(self.raiz, v)
    
    def __pertence(self, no, v):
        if no.info == v:
            return True
        else:
            p = no.prim
            while p!= None:
                if self.__pertence(p,v):
                    return True
                p = p.prox
            return False
        
    def altura(self):
        return self.__altura(self.raiz)
    
    def __altura(self, no):
        hmax = -1
        p = no.prim
        while p != None:
            h = self.__altura(p)
            if h > hmax:
                hmax = h
            p = p.prox

        return hmax + 1
    
    def pares(self, no):
        if no == None:
            return 0
        
        count = 0
        if no.info % 2 == 0:
            count += 1

        p = no.prim
        while p != None:
            count += self.pares(p)
            p = p.prox
        return count

    def folhas(self, no):
        if no == None:
            return 0

        if no.prim == None:
            return 1

        count = 0
        p = no.prim
        while p != None:
            count += self.folhas(p)
            p = p.prox
    
        return count

    def igual(self, a, b):
        if a == None and b == None:
            return True

        if a == None or b == None:
            return False

        if a.info != b.info:
            return False

        p1 = a.prim
        p2 = b.prim

        while p1 != None and p2 != None:
            if not self.igual(p1, p2):
                return False
            p1 = p1.prox
            p2 = p2.prox

        return p1 == None and p2 == None

    def copia(self, no):
        if no == None:
            return None

        novo = NoArvore(no.info)
        p = no.prim

        while p != None:
            novo_filho = self.copia(p)
            self.insereFilho(novo, novo_filho)
            p = p.prox

        return novo
