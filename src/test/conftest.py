import pytest
from domain.oltp.produtos_dao import ProdutosDao
from domain.olap.produtos_dim_dao import ProdutosDimDao

@pytest.fixture(autouse=True)
def cleanup():
    produtos_dim_dao: ProdutosDimDao = ProdutosDimDao()

    produtos_dim_dao.delete_produtos()
    count = produtos_dim_dao.select_produtos_count()
    assert count is not None
    assert count == 0

    yield


    produtos_dim_dao.delete_produtos()
    count = produtos_dim_dao.select_produtos_count()
    assert count is not None
    assert count == 0
