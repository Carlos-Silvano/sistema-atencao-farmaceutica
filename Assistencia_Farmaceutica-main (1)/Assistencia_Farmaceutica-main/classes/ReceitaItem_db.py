from .Database import Database

class ReceitaItem_db(Database):
    
    def __init__(self, db_file):
        super().__init__(db_file)
        self.name = 'receita_item'

    def init_table(self):
        """Cria a tabela 'receita_item' se ela não existir."""
        conn = None 
        try:
        
            conn = self._get_conn() # Usando _get_conn
            cursor = conn.cursor()
            
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receita_id INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                FOREIGN KEY(receita_id) REFERENCES receita(id)
            )
            """)
            
            conn.commit()
            print(f"Tabela '{self.name}' inicializada com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar tabela '{self.name}': {e}")
        finally:
            if conn:
                conn.close()


    def create(self, item):
        """Cria um novo item de receita (apenas com texto)."""
        conn = None
        try:
            
            conn = self._get_conn() # Usando _get_conn
            cursor = conn.cursor()
            
            cursor.execute(
                f"INSERT INTO {self.name} (receita_id, descricao) VALUES (?, ?)",
                (item['receita_id'], item['descricao'])
            )
            
            novo_id = cursor.lastrowid
            conn.commit()
            return novo_id
            
        except Exception as e:
            print(f"Erro ao criar item de receita: {e}")
            if conn:
                conn.rollback()
            return None
        finally:
            if conn:
                conn.close()
                
    def get_all(self):
        """Busca todos os itens da tabela 'receita_item'."""
        conn = None
        try:
            # CORREÇÃO AQUI:
            conn = self._get_conn() # Usando _get_conn
            
            
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.name}")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar todos os {self.name}: {e}")
            return []
        finally:
            if conn:
                conn.close()