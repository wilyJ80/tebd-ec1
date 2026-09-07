1. Desenhar o diagrama do Star Schema com base nas tabelas relacionais de produtos, clientes e vendas.

![dbdoc](./dbdoc/schema.svg)

2. Implementar as consultas de carga e agregação para gerar três visões analíticas distintas (ex.: Vendas por Estado, Vendas por Categoria e Faturamento por Período). 

# Preparar ambiente

1. Tenha o sqlite3 e uv instalado. [instalar uv aqui](https://docs.astral.sh/uv/getting-started/installation/)

2. Iniciar banco (Linux ou Windows com WSL/Git Bash instalados): executar `prepare.sh`

3. Inicializar projeto: `uv sync`, `uv pip install -e .`

# Executar ETL

- `uv run src/create_olap.py`

# Desenvolvimento

- Testagem com `./prepare.sh && uv run pytest`

# Consultas

1. Vendas por Estado

```
sqlite> SELECT 
    c.estado,
    SUM(f.quantidade) AS total_unidades_vendidas,
    SUM(f.valor_total) AS faturamento_total
FROM vendas_fato f
JOIN clientes_dim c ON f.sk_cliente = c.sk_cliente
GROUP BY c.estado
ORDER BY faturamento_total DESC;
╭────────┬──────────────────────┬───────────────────╮
│ estado │ total_unidades_ve... │ faturamento_total │
╞════════╪══════════════════════╪═══════════════════╡
│ SP     │                    2 │             11500 │
│ RJ     │                    1 │              3200 │
│ PR     │                    1 │              1800 │
│ BA     │                    1 │              1200 │
│ MG     │                    2 │               900 │
│ CE     │                    3 │               750 │
│ DF     │                    1 │               600 │
│ PE     │                    1 │               300 │
│ RS     │                    1 │               180 │
╰────────┴──────────────────────┴───────────────────╯
```

2. Vendas por Categoria

```
sqlite> SELECT 
    p.categoria,
    SUM(f.quantidade) AS total_unidades_vendidas,
    SUM(f.valor_total) AS faturamento_total
FROM vendas_fato f
JOIN produtos_dim p ON f.sk_produto = p.sk_produto
GROUP BY p.categoria
ORDER BY faturamento_total DESC;
╭─────────────┬──────────────────────┬───────────────────╮
│  categoria  │ total_unidades_ve... │ faturamento_total │
╞═════════════╪══════════════════════╪═══════════════════╡
│ Eletrônicos │                    3 │             12500 │
│ Componentes │                    2 │              4600 │
│ Acessórios  │                    7 │              2130 │
│ Móveis      │                    1 │              1200 │
╰─────────────┴──────────────────────┴───────────────────╯
```

3. Faturamento por Período

```
sqlite> SELECT 
    t.ano,
    t.trimestre,
    SUM(f.valor_total) AS faturamento_periodo
FROM vendas_fato f
JOIN tempo_dim t ON f.sk_tempo = t.sk_tempo
GROUP BY t.ano, t.trimestre
ORDER BY t.ano ASC, t.trimestre ASC;
╭──────┬───────────┬─────────────────────╮
│ ano  │ trimestre │ faturamento_periodo │
╞══════╪═══════════╪═════════════════════╡
│ 2024 │         1 │               20430 │
╰──────┴───────────┴─────────────────────╯
```
