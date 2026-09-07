import sqlite3
from sqlite3 import Cursor

from domain.olap.models import VendaFato


class VendasFatoDao:
    def __init__(self) -> None:
        self.db = 'olap.db'

    def delete_vendas(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            DELETE FROM vendas_fato
            """
            cursor.execute(sql)
            deleted: int = cursor.rowcount
            conn.commit()
            return deleted

    def select_vendas_count(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT COUNT(*)
            FROM vendas_fato
            """
            cursor.execute(sql)
            count: int = cursor.fetchone()[0]
            conn.commit()
            return count

    def insert_venda(self, venda_fato: VendaFato) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            INSERT INTO vendas_fato (
            id_venda, sk_cliente, sk_produto, sk_tempo, quantidade, valor_total
            ) VALUES (
            :id_venda, :sk_cliente, :sk_produto, :sk_tempo, :quantidade, :valor_total
            ) ON CONFLICT DO NOTHING
            """
            cursor.execute(sql, venda_fato.model_dump())
            inserted: int = cursor.rowcount
            conn.commit()
            return inserted
