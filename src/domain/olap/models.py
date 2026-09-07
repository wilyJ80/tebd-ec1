from pydantic import BaseModel

class Tempo(BaseModel):
    sk_tempo: int | None
    data_venda: str
    mes: int
    trimestre: int
    ano: int
