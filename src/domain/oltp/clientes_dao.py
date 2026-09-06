import sqlite3
from sqlite3 import Cursor

from domain.oltp.models import Cliente

class ClientesDao:
    def __init__(self) -> None:
        self.db = 'oltp.db'

    def select_clientes(self) -> list[Cliente]:
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT id_cliente, nome_cliente, cidade, estado
            FROM clientes
            """
            cursor.execute(sql)
            produtos: list[Cliente] = [Cliente.model_validate(dict(row)) for row in cursor.fetchall()]
            return produtos
