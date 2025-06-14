import os
from typing import List
from Produto import Produto



class InterfaceUsuario:
    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def pausar():
        input("\nPressione Enter para continuar...")
    
    @staticmethod
    def mostrar_titulo(titulo: str):
        print("=" * 60)
        print(f"  {titulo.upper()}")
        print("=" * 60)
    
    @staticmethod
    def mostrar_menu_principal() -> str:
        InterfaceUsuario.limpar_tela()
        InterfaceUsuario.mostrar_titulo("Sistema de Gerenciamento de Produtos")
        
        print("1. Cadastrar Produto")
        print("2. Listar Todos os Produtos")
        print("3. Buscar Produto")
        print("4. Atualizar Produto")
        print("5. Deletar Produto")
        print("6. Estatísticas")
        print("0. Sair")
        print("-" * 60)
        
        return input("Escolha uma opção: ").strip()
    
    @staticmethod
    def mostrar_menu_busca() -> str:
        print("\n--- BUSCAR PRODUTO ---")
        print("1. Buscar por ID")
        print("2. Buscar por Nome")
        print("3. Buscar por Categoria")
        print("0. Voltar")
        
        return input("Escolha uma opção: ").strip()
    
    @staticmethod
    def solicitar_dados_produto() -> Produto:
        print("\n--- CADASTRAR PRODUTO ---")
        
        nome = input("Nome do produto: ").strip()
        
        while True:
            try:
                preco = float(input("Preço: R$ "))
                break
            except ValueError:
                print("Por favor, digite um preço válido!")
        
        while True:
            try:
                quantidade = int(input("Quantidade: "))
                break
            except ValueError:
                print("Por favor, digite uma quantidade válida!")
        
        categoria = input("Categoria: ").strip()
        
        return Produto(nome=nome, preco=preco, quantidade=quantidade, categoria=categoria)
    
    @staticmethod
    def solicitar_dados_atualizacao(produto_atual: Produto) -> Produto:
        print(f"\n--- ATUALIZAR PRODUTO (ID: {produto_atual.id}) ---")
        print("Deixe em branco para manter o valor atual")
        
        nome = input(f"Nome [{produto_atual.nome}]: ").strip()
        if not nome:
            nome = produto_atual.nome
        
        preco_str = input(f"Preço [{produto_atual.preco:.2f}]: ").strip()
        if preco_str:
            try:
                preco = float(preco_str)
            except ValueError:
                print("Preço inválido! Mantendo valor atual.")
                preco = produto_atual.preco
        else:
            preco = produto_atual.preco
        
        quantidade_str = input(f"Quantidade [{produto_atual.quantidade}]: ").strip()
        if quantidade_str:
            try:
                quantidade = int(quantidade_str)
            except ValueError:
                print("Quantidade inválida! Mantendo valor atual.")
                quantidade = produto_atual.quantidade
        else:
            quantidade = produto_atual.quantidade
        
        categoria = input(f"Categoria [{produto_atual.categoria}]: ").strip()
        if not categoria:
            categoria = produto_atual.categoria
        
        produto_atualizado = Produto(
            id=produto_atual.id,
            nome=nome,
            preco=preco,
            quantidade=quantidade,
            categoria=categoria,
            data_cadastro=produto_atual.data_cadastro
        )
        
        return produto_atualizado
    
    @staticmethod
    def mostrar_produto(produto: Produto):
        print("\n" + "-" * 60)
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Preço: R$ {produto.preco:.2f}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Categoria: {produto.categoria}")
        print(f"Data de Cadastro: {produto.data_cadastro}")
        print("-" * 60)
    
    @staticmethod
    def mostrar_lista_produtos(produtos: List[Produto]): 
        if not produtos:
            print("\nNenhum produto encontrado!")
            return
        
        print(f"\n{len(produtos)} produto(s) encontrado(s):")
        print("-" * 60)
        
        for produto in produtos:
            print(produto)
        
        print("-" * 60)
    
    @staticmethod
    def confirmar_acao(mensagem: str) -> bool:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        return resposta == 's'