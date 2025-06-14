import sqlite3


class DatabaseConnection:
    
    def __init__(self, db_name: str = "produtos.db"):
        self.db_name = db_name
        self._init_database()
    
    def _init_database(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL,
                    categoria TEXT NOT NULL,
                    data_cadastro TEXT NOT NULL
                )
            ''')
            conn.commit()
    
    def get_connection(self):
        return sqlite3.connect(self.db_name)