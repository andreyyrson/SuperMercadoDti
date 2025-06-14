from DataBaseConnection import DatabaseConnection
from InterfaceUsuario import InterfaceUsuario
from ProdutoDao import ProdutoDAO


class SistemaProdutos:
    """Controlador principal do sistema"""
    
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.produto_dao = ProdutoDAO(self.db_connection)
        self.interface = InterfaceUsuario()
    
    def executar(self):
        while True:
            opcao = self.interface.mostrar_menu_principal()
            
            if opcao == "1":
                self._cadastrar_produto()
            elif opcao == "2":
                self._listar_produtos()
            elif opcao == "3":
                self._buscar_produto()
            elif opcao == "4":
                self._atualizar_produto()
            elif opcao == "5":
                self._deletar_produto()
            elif opcao == "6":
                self._mostrar_estatisticas()
            elif opcao == "0":
                print("\nSaindo do sistema... Até logo!")
                break
            else:
                print("Opção inválida!")
                self.interface.pausar()
    
    def _cadastrar_produto(self):
        produto = self.interface.solicitar_dados_produto()
        
        erros = produto.validar()
        if erros:
            print("\nErros encontrados:")
            for erro in erros:
                print(f"• {erro}")
        else:
            try:
                produto_id = self.produto_dao.criar(produto)
                print(f"\nProduto cadastrado com sucesso! ID: {produto_id}")
            except Exception as e:
                print(f"\nErro ao cadastrar produto: {e}")
        
        self.interface.pausar()
    
    def _listar_produtos(self):
        try:
            produtos = self.produto_dao.buscar_todos()
            self.interface.mostrar_lista_produtos(produtos)
        except Exception as e:
            print(f"\nErro ao listar produtos: {e}")
        
        self.interface.pausar()
    
    def _buscar_produto(self):
        while True:
            opcao = self.interface.mostrar_menu_busca()
            
            if opcao == "1":
                self._buscar_por_id()
                break
            elif opcao == "2":
                self._buscar_por_nome()
                break
            elif opcao == "3":
                self._buscar_por_categoria()
                break
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")
        
        self.interface.pausar()
    
    def _buscar_por_id(self):
        try:
            produto_id = int(input("Digite o ID do produto: "))
            produto = self.produto_dao.buscar_por_id(produto_id)
            
            if produto:
                self.interface.mostrar_produto(produto)
            else:
                print("\nProduto não encontrado!")
        except ValueError:
            print("ID inválido!")
        except Exception as e:
            print(f"Erro na busca: {e}")
    
    def _buscar_por_nome(self):
        try:
            nome = input("Digite o nome (ou parte do nome): ").strip()
            produtos = self.produto_dao.buscar_por_nome(nome)
            self.interface.mostrar_lista_produtos(produtos)
        except Exception as e:
            print(f"Erro na busca: {e}")
    
    def _buscar_por_categoria(self):
        try:
            categoria = input("Digite a categoria: ").strip()
            produtos = self.produto_dao.buscar_por_categoria(categoria)
            self.interface.mostrar_lista_produtos(produtos)
        except Exception as e:
            print(f"Erro na busca: {e}")
    
    def _atualizar_produto(self):
        try:
            produto_id = int(input("Digite o ID do produto a ser atualizado: "))
            produto_atual = self.produto_dao.buscar_por_id(produto_id)
            
            if not produto_atual:
                print("\nProduto não encontrado!")
                self.interface.pausar()
                return
            
            print("\nProduto atual:")
            self.interface.mostrar_produto(produto_atual)
            
            produto_atualizado = self.interface.solicitar_dados_atualizacao(produto_atual)
            
            erros = produto_atualizado.validar()
            if erros:
                print("\nErros encontrados:")
                for erro in erros:
                    print(f"• {erro}")
            else:
                if self.produto_dao.atualizar(produto_atualizado):
                    print("\nProduto atualizado com sucesso!")
                else:
                    print("\nFalha ao atualizar o produto!")
        
        except ValueError:
            print("ID inválido!")
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
        
        self.interface.pausar()
    
    def _deletar_produto(self):
        try:
            produto_id = int(input("Digite o ID do produto a ser deletado: "))
            produto = self.produto_dao.buscar_por_id(produto_id)
            
            if not produto:
                print("\nProduto não encontrado!")
                self.interface.pausar()
                return
            
            print("\nProduto a ser deletado:")
            self.interface.mostrar_produto(produto)
            
            if self.interface.confirmar_acao("Confirma a exclusão?"):
                if self.produto_dao.deletar(produto_id):
                    print("\nProduto deletado com sucesso!")
                else:
                    print("\nFalha ao deletar o produto!")
            else:
                print("\nOperação cancelada!")
        
        except ValueError:
            print("ID inválido!")
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
        
        self.interface.pausar()
    
    def _mostrar_estatisticas(self):
        try:
            total_produtos = self.produto_dao.contar_produtos()
            produtos = self.produto_dao.buscar_todos()
            
            if produtos:
                valor_total = sum(p.preco * p.quantidade for p in produtos)
                produto_mais_caro = max(produtos, key=lambda p: p.preco)
                produto_maior_estoque = max(produtos, key=lambda p: p.quantidade)
            else:
                valor_total = 0
                produto_mais_caro = None
                produto_maior_estoque = None
            
            print("\n--- ESTATÍSTICAS DO SISTEMA ---")
            print(f"Total de produtos cadastrados: {total_produtos}")
            print(f"Valor total do estoque: R$ {valor_total:.2f}")
            
            if produto_mais_caro:
                print(f"Produto mais caro: {produto_mais_caro.nome} (R$ {produto_mais_caro.preco:.2f})")
            
            if produto_maior_estoque:
                print(f"Maior estoque: {produto_maior_estoque.nome} ({produto_maior_estoque.quantidade} unidades)")
        
        except Exception as e:
            print(f"Erro ao gerar estatísticas: {e}")
        
        self.interface.pausar()