CREATE TABLE jogador
(
    id_jogador character varying(36) NOT NULL,

    jogador character varying(200) NOT NULL,
    nacionalidade character varying(20) NOT NULL,
    posicao character varying(50) NOT NULL,
    equipe character varying(50) NOT NULL,
    idade integer,
    nascimento integer,
   CONSTRAINT jogador_pkey PRIMARY KEY (id_jogador)
)