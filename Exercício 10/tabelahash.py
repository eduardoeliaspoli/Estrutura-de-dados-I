class Aluno:
    def __init__(self, nome: str, matricula: int, mediageral: float):
        self.nome = nome
        self.matricula = matricula
        self.mediageral = mediageral
        self.prox = None

class TabelaHash:
    def __init__(self, N: int):
        self.tabela = [None] * N

    def hash(self, k: int) -> int:
        return k % len(self.tabela)

    def get(self, k: int) -> Aluno:
        index = self.hash(k)
        aluno = self.tabela[index]
        while aluno != None:
            if aluno.matricula == k:
                return aluno
            aluno = aluno.prox
        return None

    def set(self, nome: str, matricula: int, mediageral: float) -> None:
        index = self.hash(matricula)
        aluno = self.tabela[index]
        while aluno is not None:
            if aluno.matricula == matricula:
                aluno.nome = nome
                aluno.mediageral = mediageral
                return
            aluno = aluno.prox
        novo_aluno = Aluno(nome, matricula, mediageral)
        novo_aluno.prox = self.tabela[index]
        self.tabela[index] = novo_aluno

    def remove(self, k: int) -> None:
        index = self.hash(k)
        aluno = self.tabela[index]
        prev_aluno = None
        while aluno is not None:
            if aluno.matricula == k:
                if prev_aluno is None:
                    self.tabela[index] = aluno.prox
                else:
                    prev_aluno.prox = aluno.prox
                return
            prev_aluno = aluno
            aluno = aluno.prox

    def __str__(self) -> str:
        resultado = ""
        for aluno in self.tabela:
            while aluno is not None:
                resultado += f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}, Média Geral: {aluno.mediageral}\n"
                aluno = aluno.prox
        return resultado
