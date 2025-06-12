
from livros import Livro
from membro import Membro
from biblioteca import Biblioteca


# --- CÓDIGO DE TESTE ---

# 1. Criar a Biblioteca
biblioteca = Biblioteca("Biblioteca Municipal de Belford Roxo")
print("\n ===============================================")
print(f"Bem-vindo à {biblioteca.nome}!")


#2. Criando os objetos Livros
livro1 = Livro(1, "Dom Casmurro", "Machado de Assis")
livro2 = Livro(2, "Crepusculo", "Marta")
livro3 = Livro(3, "Mulher invisivel", "Rafael Montes")
print("\n ===============================================\n")

#3. Adicionando os livros na biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
print("\n ===============================================\n")

#4. Criando os objetos Membros
membro1 = Membro("Amilcar", 101)
membro2 = Membro("Felipe", 102)
membro3 = Membro("Madu", 103)
membro4 = Membro("Marta", 104)


#5. Adicionando os membros na biblioteca
biblioteca.regristrar_membro(membro1)
biblioteca.regristrar_membro(membro2)
biblioteca.regristrar_membro(membro3)
biblioteca.regristrar_membro(membro4)
print("\n ===============================================")

#6. Mostrando os livros disponiveis
biblioteca.mostrar_livros_disponiveis()
print("\n ===============================================")
#7. Emprestando livro para um membro
biblioteca.realizar_emprestimo(1,102)
biblioteca.realizar_emprestimo(2, 103)
print("\n ===============================================")

#8. Checando novamente os livros disponiveis
biblioteca.mostrar_livros_disponiveis()
print("\n ===============================================")

#9. mostrar a lista de livros emprestados para os membros
membro2.mostrar_livros_emprestados()

#10. Devolver livro
biblioteca.realizar_devolucao(1)
biblioteca.mostrar_livros_disponiveis()
