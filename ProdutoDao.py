from typing import List, Optional
from DataBaseConnection import DatabaseConnection
from Produto import Produto  


class ProdutoDAO: 
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection
    
    def criar(self, produto: Produto) -> int:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO produtos (nome, preco, quantidade, categoria, data_cadastro)
                VALUES (?, ?, ?, ?, ?)
            ''', (produto.nome, produto.preco, produto.quantidade, 
                  produto.categoria, produto.data_cadastro))
            
            produto_id = cursor.lastrowid
            conn.commit()
            return produto_id
    
    def buscar_por_id(self, produto_id: int) -> Optional[Produto]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM produtos WHERE id = ?', (produto_id,))
            row = cursor.fetchone()
            
            if row:
                return Produto(
                    id=row[0], nome=row[1], preco=row[2],
                    quantidade=row[3], categoria=row[4], data_cadastro=row[5]
                )
            return None
    
    def buscar_todos(self) -> List[Produto]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM produtos ORDER BY nome')
            rows = cursor.fetchall()
            
            return [
                Produto(
                    id=row[0], nome=row[1], preco=row[2],
                    quantidade=row[3], categoria=row[4], data_cadastro=row[5]
                )
                for row in rows
            ]
    
    def buscar_por_nome(self, nome: str) -> List[Produto]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM produtos WHERE nome LIKE ? ORDER BY nome',
                (f'%{nome}%',)
            )
            rows = cursor.fetchall()
            
            return [
                Produto(
                    id=row[0], nome=row[1], preco=row[2],
                    quantidade=row[3], categoria=row[4], data_cadastro=row[5]
                )
                for row in rows
            ]
    
    def buscar_por_categoria(self, categoria: str) -> List[Produto]:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT * FROM produtos WHERE categoria LIKE ? ORDER BY nome',
                (f'%{categoria}%',)
            )
            rows = cursor.fetchall()
            
            return [
                Produto(
                    id=row[0], nome=row[1], preco=row[2],
                    quantidade=row[3], categoria=row[4], data_cadastro=row[5]
                )
                for row in rows
            ]
    
    def atualizar(self, produto: Produto) -> bool:
        if not produto.id:
            return False
        
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE produtos 
                SET nome = ?, preco = ?, quantidade = ?, categoria = ?
                WHERE id = ?
            ''', (produto.nome, produto.preco, produto.quantidade, 
                  produto.categoria, produto.id))
            
            conn.commit()
            return cursor.rowcount > 0
    
    def deletar(self, produto_id: int) -> bool:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def contar_produtos(self) -> int:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM produtos')
            return cursor.fetchone()[0]