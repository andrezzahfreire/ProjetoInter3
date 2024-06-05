CREATE TABLE indice
(
    id_indice character varying(36) NOT NULL,
    id_jogador character varying(36) NOT NULL,

    nome character varying(40),
    valor decimal,
    texto character varying(255),
    CONSTRAINT indice_pkey PRIMARY KEY (id_indice)
)