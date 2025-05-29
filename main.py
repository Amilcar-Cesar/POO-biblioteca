
from livros import Livro
from biblioteca import Biblioteca



biblioteca_geral = Biblioteca(nome ="Biblioteca Geral")

biblioteca_geral.cadastrar_livro(titulo="Glossário",autor="Geralt",ano=2015)
biblioteca_geral.cadastrar_livro(titulo="Dom Casmurro",autor="Machado de Assis",ano=1980)

Biblioteca.listar_livros(biblioteca_geral)