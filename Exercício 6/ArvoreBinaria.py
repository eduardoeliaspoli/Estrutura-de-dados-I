class NoArvoreBinaria:
    
    def __init__(self, info: int ):
        self.info = info
        self.sae = None
        self.sad = None
    
class ArvoreBinaria:
    
    def __init__(self):
        self.raiz = None

    def insere(self, v, sae, sad):
        no = NoArvoreBinaria(v)
        no.sae = sae
        no.sad = sad
        self.raiz = no
        
        return no
    
    def vazia(self):
        if self.raiz == None:
            return True
        else:
            return False
            
    def pertence(self, info):
        return self.__pertence(self.raiz, info)
    
    def __pertence(self,no,info):
        if no == None:
            return False
        else:
            return no.info == info or self.__pertence(no.sae, info) or self.__pertence(no.sad,info)
    
    def __str__(self):
        return self.__imprimePre(self.raiz)
    
    def __imprimePre(self,no):
        s = ''
        s += "<"
        if no != None:
            s = s + str(no.info)
            s = s + self.__imprimePre(no.sae)
            s = s + self.__imprimePre(no.sad)
        s+=  ">"
        return s
    
    def pares(self,no):
        if no == None:
            return 0
        if no.info % 2 == 0:
            return 1 + self.pares(no.sae) + self.pares(no.sad)
        return self.pares(no.sae) + self.pares(no.sad)
    
    def numNos(self, no : NoArvoreBinaria):
        if no == None:
            return 0
        return self.numNos(no.sae) + self.numNos(no.sad) + 1
    
    def folhas(self, no):
        if no == None:
            return 0
        elif no.sae == None and no.sad == None:
            return 1
        else:
            folhas_esquerda = self.folhas(no.sae)
            folhas_direita = self.folhas(no.sad)
            return folhas_esquerda + folhas_direita

    def imprimePos(self):
        return self.__imprimePos(self.raiz)

    def __imprimePos(self,no):
        s = ''
        if no != None:
            s = s + self.__imprimePos(no.sae)
            s = s + self.__imprimePos(no.sad)
            s = s + '<'
            s += str(no.info) 
            s = s + '>'
        return s 

    def imprimeSimetrica(self):
        return self.__imprimeSimetrica(self.raiz)

    def __imprimeSimetrica(self,no):
        s = ''
        if no != None:
            s = s + self.__imprimeSimetrica(no.sae)
            s = s + '<' 
            s = s + str(no.info)
        if no != None:
            s = s + self.__imprimeSimetrica(no.sad)
            s += '>'
        return s

    def altura(self, no):
        if no == None or no.sae == None or no.sad == None:
            return 0
        
        altura_esquerda = self.altura(no.sae) + 1
        altura_direita = self.altura(no.sad) + 1 
        if altura_esquerda > altura_direita:
            return altura_esquerda
        return altura_direita

    
    def igual(self,no,no2):
        if no == None and no2 == None:
            return True
        if no == None or no2 == None:
            return False
        if no.info != no2.info: 
            return False
        return self.igual(no.sae, no2.sae) and self.igual(no.sad, no2.sad)