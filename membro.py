class Membro:
    def __init__(self, nome, id_membro):
        self.nome = nome
        self.id_membro = id_membro
        self.livros_emprestados = []

    def pegar_livro(self, livro_objeto):
        self.livros_emprestados.append(livro_objeto)

    def devolver_livro(self, livro_objeto):
        if livro_objeto in self.livros_emprestados:
            self.livros_emprestados.remove(livro_objeto)
            return True
        else:
            raise ValueError(f"ALERTA: O membro {self.nome} tentou devolver um livro que não possuía.")
            

    def mostrar_livros_emprestados(self):
        if not self.livros_emprestados:
            print("Nenhum livro emprestado no momento.")
        else:
            for livro in self.livros_emprestados:
                print(f"- {livro}")
        print("---------------------------------------------------")

    def __str__(self):
        return f"Membro: {self.nome} | ID: {self.id_membro} | Livros emprestados: {len(self.livros_emprestados)}."