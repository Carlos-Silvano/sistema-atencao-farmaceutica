import sqlite3
from .Database import Database

class Receita_db(Database):
    def __init__(self, db_file):
        super().__init__(db_file)
        self.name = 'receita'

    def init_table(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {self.name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            nome_medico TEXT NOT NULL,
            crm_medico TEXT NOT NULL,
            data_emissao TEXT NOT NULL,
            FOREIGN KEY(paciente_id) REFERENCES paciente(id) ON DELETE CASCADE
        );
        '''
        return super().init_table(sql)

    def create(self, receita):
        """Cria uma nova receita e RETORNA O SEU ID."""
        conn = None
        try:
            # CORREÇÃO AQUI:
            conn = self._get_conn() # Usando _get_conn
            cursor = conn.cursor()
            
            cursor.execute(
                "INSERT INTO receita (paciente_id, nome_medico, crm_medico, data_emissao) VALUES (?, ?, ?, ?)",
                (receita['paciente_id'], receita['nome_medico'], receita['crm_medico'], receita['data_emissao'])
            )
            
            novo_id = cursor.lastrowid 
            conn.commit()
            
            print(f"Receita criada com ID: {novo_id}")
            return novo_id
            
        except Exception as e:
            print(f"Erro ao criar receita: {e}")
            if conn:
                conn.rollback() 
            return None
            
        finally:
            if conn:
                conn.close()
                
    def get_all(self):
        """Busca todas as receitas da tabela 'receita'."""
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
                
    def delete(self, receita_id):
        try:
            conn = self._get_conn()

            # cur.execute(sql_select_receita_ids, (paciente_id,))
            # receita_ids = cur.fetchall()
            
            self._delete_receitaitem(conn, receita_id)

            self._delete_receita(conn, receita_id)

            conn.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"ERRO CRÍTICO na deleção em cascata (ROLLBACK): {e}")
            if conn:
                conn.rollback()
            return False
            
        finally:
            conn.close()

    def _delete_receita(self, conn, paciente_id):
        sql = "DELETE FROM receita WHERE id = ?"
        conn.execute(sql, (paciente_id,))


    def _delete_receitaitem(self, conn, receita_id):
        sql = "DELETE FROM receita_item WHERE receita_id = ?"
        conn.execute(sql, (receita_id,))
