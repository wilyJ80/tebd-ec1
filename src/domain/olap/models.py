from pydantic import BaseModel

class Tempo(BaseModel):
    sk_tempo: int | None
    data_venda: str
    mes: int
    trimestre: int
    ano: int

class VendaFato(BaseModel):
    id_venda: int
    sk_cliente: int
    sk_produto: int
    sk_tempo: int
    quantidade: int
    valor_total: int
