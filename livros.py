from dataclasses import dataclass

@dataclass

class Livro():
    titulo: str
    autor: str
    ano: int

    def detalhes(self):
        print(f"Título do livro: {self.titulo} | Autor:{self.autor} | Ano de publicação: {self.ano}")


