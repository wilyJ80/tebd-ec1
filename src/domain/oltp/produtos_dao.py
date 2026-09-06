import sqlite3
from sqlite3 import Cursor

from domain.oltp.models import Produto


class ProdutosDao:
    def __init__(self) -> None:
        self.db = 'oltp.db'

    def select_produtos(self) -> list[Produto]:
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT id_produto, nome_produto, categoria, preco
            FROM produtos
            """
            cursor.execute(sql)
            produtos: list[Produto] = [Produto.model_validate(dict(row)) for row in cursor.fetchall()]
            return produtos
