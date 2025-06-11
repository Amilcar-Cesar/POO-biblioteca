class Livro:
    def __init__(self, titulo, autor, id_livro):
        self.titulo = titulo
        self.autor = autor
        self.id_livro = id_livro
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
           self.disponivel = print(f"O livro'{self.titulo} foi marcado como emprestado.")
            

    def devolver(self):
        pass

#_____________________________________________________________________

class Membro:
    def __init__(self, nome, id_membro, livros_emprestdos):
        self.nome = nome
        self.id_membro = id_membro
        self.livros_emprestados = []

    def pegar_livro(self, titulo):
        pass

    def retornar_livro(self):
        pass

#______________________________________________________________________

class Biblioteca:
    def __init__(self, nome):
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self, livro):
        if livro in self.catalogo:
            raise ValueError("O Livro já está em nosso catálogo!")
            return 
        
        self.catalogo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao catálogo.")

    def regristrar_membro(self, membro):
        if membro in self.membros:
            raise ValueError("O membro já faz parte desta biblioteca!")
            return
        self.membros.append(membro)
        print(f"Membro {membro.nome} registrado com sucesso.")

    def mostrar_livros_disponiveis(self):
        print("\n --- Livros Disponíveis ---")
        livros_encontrados = False
        for livro in self.catalogo:
            if livro.disponivel:
                print(f"- Título: {livro.titulo}, Autor: {livro.autor}.")
                livros_encontrados = True
            
            if not livros_encontrados:
                print("Nennhum livro disponível no momento.")