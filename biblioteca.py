class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self, livro):
        if livro in self.catalogo:
            raise ValueError("O Livro já está em nosso catálogo!")
            
        
        self.catalogo.append(livro)
        print(f"Livro  adicionado ao catálogo.")

    def regristrar_membro(self, membro):
        if membro in self.membros:
            raise ValueError("O membro já faz parte desta biblioteca!")
            
        self.membros.append(membro)
        print(f"Membro {membro.nome} registrado com sucesso.")

    def mostrar_livros_disponiveis(self):
        print("\n --- Livros Disponíveis ---")
        
        #defino uma variavel booleana como false para inicalizar a consulta.
        livros_encontrados = False
        
        for livro in self.catalogo:
            if livro.disponivel:
                print(f"- Título: {livro.titulo} | Autor: {livro.autor}.")
                #defino a variavel como True para ter um tratamento caso ela permaneça False ao fim do laço For
                livros_encontrados = True
        #se o laço For nao for realizado e a variavel continuar sendo False.    
        if not livros_encontrados:
            print("Nennhum livro disponível no momento.")

    def realizar_emprestimo(self, id_livro, id_membro):
        livro_encontrado = None
        membro_encontrado = None
        #busca na lista de livros através do ID o livro que queremos emprestar.
        for livro in self.catalogo:
            if livro.id_livro == id_livro:
                livro_encontrado = livro
                break

        #busca na lista de membros da biblioteca o membro solicitado para realizar o emprestimo.        
        for membro in self.membros:
            if membro.id_membro == id_membro:
                membro_encontrado = membro
                break
        
        
        if not livro_encontrado:
            raise ValueError("Erro: Livro não encontrado.")
            

        if not membro_encontrado:
            raise ValueError("Erro: Membro não encontrado.")
            

        if livro_encontrado.emprestar():
            
            membro_encontrado.pegar_livro(livro_encontrado)
            print(f"Empréstimo realizado com sucesso para o membro {membro_encontrado.nome}.")
        else:
            print(f"Não foi possível realizar o empréstimo para {membro_encontrado.nome}.")

    

    def realizar_devolucao(self, id_livro):
        """
        Orquestra a operação de devolução de um livro.
        """
        print(f"\nTentando realizar a devolução do livro com ID: {id_livro}...")
        livro_a_devolver = None
        membro_que_possui = None

        # Passo 1: Encontrar o objeto Livro no catálogo principal
        for livro in self.catalogo:
            if livro.id_livro == id_livro:
                livro_a_devolver = livro
                break
        
        if not livro_a_devolver:
            raise ValueError(f"ERRO: Livro com ID {id_livro} não encontrado em nosso sistema.")
            

        # Passo 2: Verificar se o livro está de fato emprestado
        if livro_a_devolver.disponivel:
            raise ValueError(f"ERRO: O livro '{livro_a_devolver.titulo}' já consta como disponível.")
            

        # Passo 3: Encontrar qual membro está com o livro
        for membro in self.membros:
            if livro_a_devolver in membro.livros_emprestados:
                membro_que_possui = membro
                break
        
        if not membro_que_possui:
            raise ValueError(f"ALERTA DE SISTEMA: O livro '{livro_a_devolver.titulo}' está como emprestado, mas não foi encontrado com nenhum membro.")
            

        # Passo 4: Orquestrar a devolução
        # A Biblioteca pede para o livro se marcar como disponível
        livro_a_devolver.devolver()
        # A Biblioteca pede para o membro remover o livro da sua lista
        membro_que_possui.devolver_livro(livro_a_devolver)

        print(f"Devolução concluída! O membro {membro_que_possui.nome} devolveu o livro '{livro_a_devolver.titulo}'.")

    
