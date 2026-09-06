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
            )
            """
            cursor.execute(sql, produto.model_dump())
            inserted: int = cursor.rowcount
            conn.commit()
            return inserted
