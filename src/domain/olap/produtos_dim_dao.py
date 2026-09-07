import sqlite3
from sqlite3 import Cursor

from domain.oltp.models import Produto


class ProdutosDimDao:
    def __init__(self) -> None:
        self.db = 'olap.db'

    def delete_produtos(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            DELETE FROM produtos_dim
            """
            cursor.execute(sql)
            deleted: int = cursor.rowcount
            conn.commit()
            return deleted

    def select_produtos_count(self) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT COUNT(*)
            FROM produtos_dim
            """
            cursor.execute(sql)
            count: int = cursor.fetchone()[0]
            conn.commit()
            return count

    def insert_produto(self, produto: Produto) -> int:
        with sqlite3.connect(self.db) as conn:
            cursor: Cursor = conn.cursor()
            sql: str = """
            INSERT INTO produtos_dim (
            id_produto, nome_produto, categoria, preco
            ) VALUES (
            :id_produto, :nome_produto, :categoria, :preco
            ) ON CONFLICT DO NOTHING
            """
            cursor.execute(sql, produto.model_dump())
            inserted: int = cursor.rowcount
            conn.commit()
            return inserted

    def select_produto_by_id_produto(self, id_produto: int) -> Produto:
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            cursor: Cursor = conn.cursor()
            sql: str = """
            SELECT sk_produto, id_produto, nome_produto, categoria, preco
            FROM produtos_dim
            WHERE id_produto = ?
            """
            cursor.execute(sql, (id_produto,))
            row = cursor.fetchone()
            produto: Produto = Produto.model_validate(dict(row))
            conn.commit()
            return produto

