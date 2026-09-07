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

    def select_cliente_by_id_cliente(self, id_cliente: int) -> Cliente:
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT sk_cliente, id_cliente, nome_cliente, cidade, estado
            FROM clientes_dim
            WHERE id_cliente = ?
            """
            cursor.execute(sql, (id_cliente,))
            row = cursor.fetchone()
            cliente: Cliente = Cliente.model_validate(dict(row))
            conn.commit()
            return cliente

