from datetime import datetime
from domain.olap.produtos_dim_dao import ProdutosDimDao
from domain.olap.clientes_dim_dao import ClientesDimDao
from domain.oltp.models import Produto, Cliente, Venda
from domain.olap.models import Tempo
from domain.olap.tempo_dim_dao import TempoDimDao
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

        tempo: Tempo = Tempo(
            sk_tempo=None,
            data_venda=venda.data_venda,
            mes=month,
            trimestre=quarter,
            ano=year
        )

        tempo_dim_dao: TempoDimDao = TempoDimDao()
        rowcount: int = tempo_dim_dao.insert_tempo(tempo)
        assert rowcount is not None
        assert rowcount > 0
        count: int = tempo_dim_dao.select_tempo_count()
        assert count > 0

        # Lookup SKs

        ## Vendas SK
        venda_tempo: Tempo = tempo_dim_dao.select_by_data_venda(data_venda=venda.data_venda)
        assert venda_tempo is not None
        assert isinstance(venda_tempo, Tempo)

        ## Clientes SK
        assert venda.id_cliente is not None
        venda_cliente: Cliente = clientes_dim_dao.select_cliente_by_id_cliente(venda.id_cliente)
        assert venda_cliente is not None
        assert isinstance(venda_cliente, Cliente)

        ## Produtos SK
        assert venda.id_produto is not None
        venda_produto: Produto = produtos_dim_dao.select_produto_by_id_produto(venda.id_produto)
        assert venda_produto is not None
        assert isinstance(venda_produto, Produto)

    # Load into fact table
