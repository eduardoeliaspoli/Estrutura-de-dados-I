class NoArvoreBinaria:
    
    def __init__(self, info: int):
        self.info = info
        self.sae = None
        self.sad = None
    
class ArvoreBinaria:
    
    def __init__(self):
        self.raiz = None
    
    def insere(self, valor):
        self.raiz = self.__insereAux(self.raiz, valor)

    def __insereAux(self, no, valor):
        if no is None:
            no = NoArvoreBinaria(valor)
        else:
            if valor < no.info:
                no.sae = self.__insereAux(no.sae, valor)
            else:
                no.sad = self.__insereAux(no.sad, valor)
        return no

    def busca(self, valor):
        return self.__buscaAux(self.raiz, valor)
    
    def __buscaAux(self, no, valor):
        if no is None or no.info == valor:
            return no
        if valor < no.info:
            return self.__buscaAux(no.sae, valor)
        else:
            return self.__buscaAux(no.sad, valor)

    def retira(self, valor):
        self.raiz = self.__retiraAux(self.raiz, valor)

    def __retiraAux(self, no, valor):
        if no is None:
            return None
        if valor < no.info:
            no.sae = self.__retiraAux(no.sae, valor)
        elif valor > no.info:
            no.sad = self.__retiraAux(no.sad, valor)
        else:
            if no.sae is None:
                return no.sad
            elif no.sad is None:
                return no.sae
            else:
                p = no.sae
                while p.sad is not None:
                    p = p.sad
                no.info = p.info
                p.info = valor
                no.sae = self.__retiraAux(no.sae, valor)
        return no

    def __str__(self):
        return self.__imprimeEmOrdem(self.raiz)

    def __imprimeEmOrdem(self, no):
        if no is None:
            return ""
        resultado = "<"
        resultado += self.__imprimeEmOrdem(no.sae)
        resultado += str(no.info) + ">"
        resultado += self.__imprimeEmOrdem(no.sad)
        return resultado.strip()
