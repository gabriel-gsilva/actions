-- Cria database
CREATE DATABASE developer;
USE developer;

-- Cria tabela que recebe as 'url' para monitoramento
CREATE TABLE developer.ACTION_URL(
ID_URL INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
NAME_URL TEXT
);

-- Insere os valores, importante usar o site infomoney, pois o site possui pouco codigo html
INSERT INTO ACTION_URL(NAME_URL)
VALUES('https://www.infomoney.com.br/cotacoes/banco-inter-bidi4/');

INSERT INTO ACTION_URL(NAME_URL)
VALUES('https://www.infomoney.com.br/cotacoes/itau-unibanco-itub3f/');

-- Cria tabela para o algoritmo salvar o valor das ações
CREATE TABLE developer.ACTION_MONITORING(
ID_ACTION INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
NAME_ACTION VARCHAR(30) NOT NULL,
CODE_ACTION VARCHAR(10) NOT NULL,
VALUE_ACTION NUMERIC(4,2) NOT NULL,
DATE_ACTION TIMESTAMP NOT NULL
);