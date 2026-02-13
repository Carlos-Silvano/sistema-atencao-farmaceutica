import sqlite3
from .Database import Database

class Paciente_db(Database):
    def __init__(self,db_file):
        super().__init__(db_file)
        self.name="paciente" 

    def init_table(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {self.name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nascimento TEXT NOT NULL,
            sexo TEXT NOT NULL,
            telefone TEXT,
            email TEXT UNIQUE,
            endereco TEXT,
            doencas TEXT,
            alergias TEXT
        );
        '''
        return super().init_table(sql)

    def create(self,inputs):
        return super().create(self.name,inputs)

    def get_all(self):
        """Busca todos os pacientes da tabela 'paciente'."""
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

    def delete(self, paciente_id):
        try:
            conn = self._get_conn()
            cur = conn.cursor()

            sql_select_receita_ids = "SELECT id FROM receita WHERE paciente_id = ?"
            cur.execute(sql_select_receita_ids, (paciente_id,))
            receita_ids = cur.fetchall()
            
            self._delete_receitaitem(cur, receita_ids)

            self._delete_receita(cur, paciente_id)

            self._delete_paciente(cur, paciente_id)

            conn.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"ERRO CRÍTICO na deleção em cascata (ROLLBACK): {e}")
            if conn:
                conn.rollback()
            return False
            
        finally:
            conn.close()

    def _delete_paciente(self, cur, paciente_id):
        sql = "DELETE FROM paciente WHERE id = ?"
        cur.execute(sql, (paciente_id,))
    
    def _delete_receita(self, cur, paciente_id):
        sql = "DELETE FROM receita WHERE paciente_id = ?"
        cur.execute(sql, (paciente_id,))


    def _delete_receitaitem(self, cur, receita_ids_tuplas):
        if not receita_ids_tuplas:
            return
        
        ids_list = [r[0] for r in receita_ids_tuplas]

        placeholders = ', '.join('?' * len(ids_list))
        sql = f"DELETE FROM receita_item WHERE receita_id IN ({placeholders})"
        
        cur.execute(sql, ids_list)