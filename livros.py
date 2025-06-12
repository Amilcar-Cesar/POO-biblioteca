class Livro:
    def __init__(self, id_livro, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.id_livro = id_livro
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False 
            print(f"O livro '{self.titulo}' foi marcado como emprestado.")
            return True
        else:
            raise ValueError(f"O livro {self.titulo} não está disponível para empréstimo.") 
            
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel	 = True
            print(f'O livro {self.titulo} foi devolvido e está disponível.')
            return True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"ID: {self.id_livro} | Título: {self.titulo} | Autor: {self.autor} | Status: {status}."