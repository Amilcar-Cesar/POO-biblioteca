from dataclasses import dataclass, field
from typing import List
from livros import Livro


@dataclass

class Biblioteca:
    nome: str
    livros: List[Livro] = field(default_factory=list)


    def cadastrar_livro(self, titulo, autor, ano):
        novo_livro = Livro(titulo=titulo, autor=autor, ano=ano)
                
        self.livros.append(novo_livro)
        return novo_livro
            
    def listar_livros(self):
        if not self.livros:
            print(f"A biblioteca {self.nome} não possui livros cadastrados.")
            return
                
        for livro in self.livros:
            livro.detalhes()



    