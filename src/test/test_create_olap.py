from datetime import datetime
from domain.olap.produtos_dim_dao import ProdutosDimDao
from domain.olap.clientes_dim_dao import ClientesDimDao
from domain.oltp.models import Produto, Cliente, Venda
from domain.oltp.produtos_dao import ProdutosDao
from domain.oltp.clientes_dao import ClientesDao
from domain.oltp.vendas_dao import VendasDao


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
    count: int = clientes_dim_dao.select_clientes_count()
    assert count > 0

    # Vendas OLTP extraction
    vendas_dao: VendasDao = VendasDao()
    vendas: list[Venda] = vendas_dao.select_vendas()
    assert vendas is not None
    assert isinstance(vendas, list)
    assert all(isinstance(v, Venda) for v in vendas)
    assert len(vendas) > 1
    for venda in vendas:

        ## Time dimension population
        dt = datetime.strptime(venda.data_venda, "%Y-%m-%d")
        month = dt.month
        quarter = (dt.month - 1) // 3 + 1
        year = dt.year

    # Lookup SKs

    # Load into fact table
