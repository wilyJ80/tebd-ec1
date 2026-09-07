import pytest

from domain.olap.produtos_dim_dao import ProdutosDimDao
from domain.olap.clientes_dim_dao import ClientesDimDao
from domain.olap.vendas_fato_dao import VendasFatoDao

def cleanup():
    produtos_dim_dao: ProdutosDimDao = ProdutosDimDao()
    produtos_dim_dao.delete_produtos()
    count = produtos_dim_dao.select_produtos_count()
    assert count is not None
    assert count == 0
    
    clientes_dim_dao: ClientesDimDao = ClientesDimDao()
    clientes_dim_dao.delete_clientes()
    count = clientes_dim_dao.select_clientes_count()
    assert count is not None
    assert count == 0

    vendas_fato_dao: VendasFatoDao = VendasFatoDao()
    vendas_fato_dao.delete_vendas()
    count = vendas_fato_dao.select_vendas_count()
    assert count is not None
    assert count == 0

@pytest.fixture(autouse=True)
def reset():
    cleanup()
    yield
    cleanup()
