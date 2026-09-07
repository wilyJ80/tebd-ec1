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

class Venda(BaseModel):
    id_venda: int | None
    id_cliente: int | None
    id_produto: int | None
    data_venda: str
    quantidade: int
    valor_total: int
