CREATE DATABASE projeto_vendas;

USE projeto_vendas;

CREATE TABLE produtos ( 
    produtos_id VARCHAR(10) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    PRIMARY KEY(produtos_id)
);

CREATE TABLE vendas (
    pedido INT NOT NULL AUTO_INCREMENT,
    item_id VARCHAR(10) NOT NULL,
    forma_de_pagamento VARCHAR(20) NOT NULL,
    parcelas INT NOT NULL,-
    juros INT NOT NULL,
    desconto INT NOT NULL,
    preco_de_venda INT NOT NULL,
    frete_empresa INT NOT NULL,
    frete_cliente INT NOT NULL,
    frete_total INT NOT NULL,
    uf VARCHAR(10)
    produtos_id VARCHAR(10) NOT NULL,
    PRIMARY KEY(pedido),
    FOREIGN KEY(item_id) REFERENCES produtos (produtos_id)
);

SHOW TABLES;
