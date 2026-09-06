from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int | None
    nome_produto: str
    categoria: str | None
    preco: int

class Cliente(BaseModel):
    id_cliente: int | None
    nome_cliente: str
    cidade: str | None
    estado: str | None
