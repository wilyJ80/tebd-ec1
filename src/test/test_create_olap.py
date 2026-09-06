from domain.oltp.produtos_dao import ProdutosDao
from domain.oltp.models import Produto
from domain.olap.produtos_dim_dao import ProdutosDimDao

def test_create_olap():
    # Produtos dimension
    produtos_dao: ProdutosDao = ProdutosDao()
    produtos: list[Produto] = produtos_dao.select_produtos()
    assert produtos is not None
    assert isinstance(produtos, list)
    assert all(isinstance(p, Produto) for p in produtos)
    assert len(produtos) > 1

    produtos_dim_dao: ProdutosDimDao = ProdutosDimDao()
    for produto in produtos:
        rowcount: int = produtos_dim_dao.insert_produto(produto)
        assert rowcount is not None
        assert rowcount > 0
