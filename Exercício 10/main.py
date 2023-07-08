from tabelahash import TabelaHash
def main():
    tabela = TabelaHash(11)

    tabela.set("João", 1234, 8.5) 
    tabela.set("Maria", 5678, 9.2)
    tabela.set("Pedro", 9012, 7.8)

    print("Conteúdo da tabela hash:")
    print(tabela)

    matricula = 5678
    aluno = tabela.get(matricula)
    if aluno:
        print(f"Aluno encontrado: Nome: {aluno.nome}, Matrícula: {aluno.matricula}, Média Geral: {aluno.mediageral}")
    else:
        print(f"Aluno com matrícula {matricula} não encontrado.")

    matricula_remover = 9012
    tabela.remove(matricula_remover)
    print(f"Após remover o aluno com matrícula {matricula_remover}:")
    print(tabela)

if __name__ == "__main__":
    main()