import sqlite3

class Database:
    def __init__(self, db_file):
        """Salva o nome do arquivo do banco quando a classe é criada."""
        self.db_file = db_file

    def _get_conn(self):
        """Função privada para criar e configurar a conexão."""
        conn = sqlite3.connect(self.db_file)
        conn.execute("PRAGMA foreign_keys = 1")
        conn.row_factory = sqlite3.Row
        return conn

    def init_table(self, sql):
        try:
            conn = self._get_conn()
            conn.execute(sql)
            print("Tabela inicializada com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar o banco: {e}")
        finally:
            conn.close()

    def get_all(self, sql):
        try:
            conn = self._get_conn()
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            return []  
        finally:
            conn.close()
    def dict_factory(self, cursor, row):
        """Converte a tupla do SQLite em um dicionário (ex: row['nome'])."""
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    def create(self, table, inputs):
        """Adiciona um novo registro ao banco de dados."""
        chaves = list(inputs.keys())
        n = len(chaves)
        
        # Monta a parte das colunas
        sql = f'INSERT INTO {table} ('
        for i in range(n-1):
            sql = sql + chaves[i] + ", "
        sql = sql + chaves[-1] + ")"
        
        # Monta a parte dos VALUES
        placeholders = "?, " * (n-1) + "?"
        sql = sql + f" VALUES ({placeholders})"
        
        values = tuple(inputs.values())
        
        try:
            conn = self._get_conn()
            conn.execute(sql, values)
            conn.commit()
            return True  
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
            return False  
        except Exception as e:
            print(f"Erro ao criar {table}: {e}")
            return False  
        finally:
            conn.close()

    def delete(self,table,id):
        sql = f"DELETE FROM {table} WHERE id = ?"
        try:
            conn = self._get_conn()
            conn.execute(sql, (id,))
            conn.commit()
            return True  
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
            return False  
        except Exception as e:
            print(f"Erro ao deletar id {id} da tabela {table}: {e}")
            return False  
        finally:
            conn.close()