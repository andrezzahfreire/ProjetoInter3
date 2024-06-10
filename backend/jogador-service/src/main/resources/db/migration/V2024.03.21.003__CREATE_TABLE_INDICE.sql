CREATE TABLE indice -- Criação da tabela de índice
(
    id_indice character varying(36) NOT NULL, -- Identificador do índice
    id_jogador character varying(36) NOT NULL, -- Identificador do jogador

    nome character varying(40), -- Nome do índice
    valor decimal, -- Valor do índice
    texto character varying(255), -- Texto do índice
    CONSTRAINT indice_pkey PRIMARY KEY (id_indice) -- Chave primária da tabela
)