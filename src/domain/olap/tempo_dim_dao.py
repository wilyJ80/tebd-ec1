import sqlite3
from sqlite3 import Cursor

from domain.olap.models import Tempo

class TempoDimDao:
    def __init__(self) -> None:
        self.db = 'olap.db'

    def delete_tempo(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            DELETE FROM tempo_dim
            """
            cursor.execute(sql)
            deleted: int = cursor.rowcount
            conn.commit()
            return deleted

    def select_tempo_count(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT COUNT(*)
            FROM tempo_dim
            """
            cursor.execute(sql)
            count: int = cursor.fetchone()[0]
            conn.commit()
            return count

    def insert_tempo(self, tempo: Tempo) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            INSERT INTO tempo_dim (
            data_venda, mes, trimestre, ano
            ) VALUES (
            :data_venda, :mes, :trimestre, :ano
            ) ON CONFLICT DO NOTHING
            """
            cursor.execute(sql, tempo.model_dump())
            inserted: int = cursor.rowcount
            conn.commit()
            return inserted
