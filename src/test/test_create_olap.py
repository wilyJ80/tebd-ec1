from domain.olap.produtos_dim_dao import ProdutosDimDao
from domain.olap.clientes_dim_dao import ClientesDimDao
from domain.oltp.models import Produto, Cliente
from domain.oltp.produtos_dao import ProdutosDao
from domain.oltp.clientes_dao import ClientesDao


def test_create_olap():
    # Produtos dimension migration
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

    count: int = produtos_dim_dao.select_produtos_count()
    assert count > 0

    # Clientes dimension migration
    clientes_dao: ClientesDao = ClientesDao()
    clientes: list[Cliente] = clientes_dao.select_clientes()
    assert clientes is not None
    assert isinstance(clientes, list)
    assert all(isinstance(c, Cliente) for c in clientes)
    assert len(clientes) > 1

    clientes_dim_dao: ClientesDimDao = ClientesDimDao()
    for cliente in clientes:
        rowcount: int = clientes_dim_dao.insert_cliente(cliente)
        assert rowcount is not None
        assert rowcount > 0
