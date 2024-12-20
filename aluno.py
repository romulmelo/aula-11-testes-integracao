class AlunoClass:
    def __init__(self, nome, sobrenome, nota):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrar_aluno(self):
        return f"Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota}"

    def salvar(self, conexao, colecao):
        doc = self.__dict__
        resultado = conexao[colecao].insert_one(doc)
        return resultado.acknowledged
