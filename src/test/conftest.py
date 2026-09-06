import pytest

from domain.olap.produtos_dim_dao import ProdutosDimDao
from domain.olap.clientes_dim_dao import ClientesDimDao

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

@pytest.fixture(autouse=True)
def reset():
    cleanup()

    yield

    cleanup()
