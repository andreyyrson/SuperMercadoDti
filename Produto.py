import sqlite3
import os
from datetime import datetime
from typing import List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Produto:
    id: Optional[int] = None
    nome: str = ""
    preco: float = 0.0
    quantidade: int = 0
    categoria: str = ""
    data_cadastro: Optional[str] = None
    
    def __post_init__(self):
        if self.data_cadastro is None:
            self.data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def validar(self) -> List[str]:
        erros = []
        
        if not self.nome or len(self.nome.strip()) < 3:
            erros.append("Nome deve ter pelo menos 3 caracteres")
        
        if self.preco < 0:
            erros.append("Preço não pode ser negativo")
        
        if self.quantidade < 0:
            erros.append("Quantidade não pode ser negativa")
        
        if not self.categoria or len(self.categoria.strip()) < 2:
            erros.append("Categoria deve ter pelo menos 2 caracteres")
        
        return erros
    
    def __str__(self):
        return f"ID: {self.id} | {self.nome} | R$ {self.preco:.2f} | Qtd: {self.quantidade} | {self.categoria}"