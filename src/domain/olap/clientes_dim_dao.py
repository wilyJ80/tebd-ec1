import sqlite3
from sqlite3 import Cursor
from domain.oltp.models import Cliente


class ClientesDimDao:
    def __init__(self) -> None:
        self.db = 'olap.db'

    def delete_clientes(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            DELETE FROM clientes_dim
            """
            cursor.execute(sql)
            deleted: int = cursor.rowcount
            conn.commit()
            return deleted

    def select_clientes_count(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT COUNT(*)
            FROM clientes_dim
            """
            cursor.execute(sql)
            count: int = cursor.fetchone()[0]
            conn.commit()
            return count

    def insert_cliente(self, cliente: Cliente) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            INSERT INTO clientes_dim (
            id_cliente, nome_cliente, cidade, estado
            ) VALUES (
            :id_cliente, :nome_cliente, :cidade, :estado
            ) ON CONFLICT DO NOTHING
            """
            cursor.execute(sql, cliente.model_dump())
            inserted: int = cursor.rowcount
            conn.commit()
            return inserted
