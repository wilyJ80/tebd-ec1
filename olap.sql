CREATE TABLE IF NOT EXISTS tempo_dim (
	sk_tempo INTEGER PRIMARY KEY AUTOINCREMENT,
	data_venda DATE NOT NULL,
	mes INT NOT NULL,
	trimestre INT NOT NULL,
	ano INT NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos_dim (
	sk_produto INTEGER PRIMARY KEY AUTOINCREMENT,
	id_produto INT NOT NULL,
    nome_produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS clientes_dim (
	sk_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
	id_cliente INT NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    cidade VARCHAR(50),
    estado VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS vendas_fato (
	sk_venda INTEGER PRIMARY KEY AUTOINCREMENT,
	id_venda INT NOT NULL,

    sk_cliente INT NOT NULL,
    sk_produto INT NOT NULL,
	sk_tempo INT NOT NULL,

    quantidade INT NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,

    FOREIGN KEY (sk_cliente) REFERENCES clientes_dim(sk_cliente),
    FOREIGN KEY (sk_produto) REFERENCES produtos_dim(sk_produto)
	FOREIGN KEY(sk_tempo) REFERENCES tempo_dim(sk_tempo)
);
