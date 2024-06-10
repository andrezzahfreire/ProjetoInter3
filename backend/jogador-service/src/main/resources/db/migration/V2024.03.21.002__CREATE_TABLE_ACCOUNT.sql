CREATE TABLE jogador -- Criação da tabela de jogador
(
    id_jogador character varying(36) NOT NULL, -- Identificador do jogador

    jogador character varying(200) NOT NULL, -- Nome do jogador
    nacionalidade character varying(20) NOT NULL, -- Nacionalidade do jogador
    posicao character varying(50) NOT NULL, -- Posição do jogador
    equipe character varying(50) NOT NULL, -- Equipe do jogador
    idade integer, -- Idade do jogador
    nascimento integer, -- Data de nascimento do jogador
   CONSTRAINT jogador_pkey PRIMARY KEY (id_jogador) -- Chave primária da tabela
)