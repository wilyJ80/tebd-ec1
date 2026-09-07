import sqlite3
from sqlite3 import Cursor

from domain.oltp.models import Venda

class VendasDao:
    def __init__(self) -> None:
        self.db = 'oltp.db'

    def select_vendas(self) -> list[Venda]:
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT id_venda, id_cliente, id_produto, data_venda, quantidade, valor_total
            FROM vendas
            """
            cursor.execute(sql)
            vendas: list[Venda] = [Venda.model_validate(dict(row)) for row in cursor.fetchall()]
            return vendas

