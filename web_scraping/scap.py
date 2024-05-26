# IMPORTACAO DE MODULOS
from bs4 import BeautifulSoup as bs # modulo para processar html
import pandas as pd # mexe com tabelas
import requests # acessa urls e extrai o codigo deles
from parsers import *
from constantes import *

# LISTAS DE URLS E IDS DAS TABELAS
mapa_urls = {
    0: {
        "url": "https://fbref.com/pt/comps/24/2023/stats/2023-Serie-A-estatisticas",
        "table_id": "stats_standard",
        "parser": payload_standard,
    },
    1: {
        "url": "https://fbref.com/pt/comps/24/2023/passing/2023-Serie-A-estatisticas",
        "table_id": "stats_passing",
        "parser": payload_passing,
    },
    2: {
        "url": "https://fbref.com/pt/comps/24/2023/keepersadv/2023-Serie-A-estatisticas",
        "table_id": "stats_keeper_adv",
        "parser": payload_keepersadv,
    },
    3: {
        "url": "https://fbref.com/pt/comps/24/2023/shooting/2023-Serie-A-estatisticas",
        "table_id": "stats_shooting",
        "parser": payload_shooting,
    },
    4: {
        "url": "https://fbref.com/pt/comps/24/2023/passing_types/2023-Serie-A-estatisticas",
        "table_id": "stats_passing_types",
        "parser": payload_passing_types,
    },
    5: {
        "url": "https://fbref.com/pt/comps/24/2023/gca/2023-Serie-A-estatisticas",
        "table_id": "stats_gca",
        "parser": payload_gca,
    },
    6: {
        "url": "https://fbref.com/pt/comps/24/2023/possession/2023-Serie-A-estatisticas",
        "table_id": "stats_possession",
        "parser": payload_possession,
    },
    7: {
        "url": "https://fbref.com/pt/comps/24/2023/playingtime/2023-Serie-A-estatisticas",
        "table_id": "stats_playing_time",
        "parser": payload_playingtime,
    },
    8: {
        "url": "https://fbref.com/pt/comps/24/2023/misc/2023-Serie-A-estatisticas",
        "table_id": "stats_misc",
        "parser": payload_misc,
    },
}

sesh = requests.Session() # inicializa uma sessao no modulo requests

dados_gerais = []

for i, info in mapa_urls.items(): # itera sobre a lista de urls, devolve tuplas (INDICE, VALOR) da lista
    
    print(f"{info['url']}: importando")
    
    # pega o codigo html da url e remove marcadores de comentarios, transformando todo comentario em 'parte do codigo' <-- A TABELA TAVA ESCONDIDA NOS COMENTARIOS    
    response = requests.get(info['url']).text.replace('<!--', '').replace('-->', '')
    
    # transforma o codigo html em um objeto BeautifulSoup, que permite a busca de elementos html
    soup = bs(response, 'html.parser')
    
    # no objeto BS, procura a tabela com o id especificado na lista de ids com o mesmo indice do URL
    table_w_data = soup.select_one(f'table#{info['table_id']}')
    
    # usa PANDAS para converter o HTML da tabela em uma DATAFRAME python
    df = pd.read_html(str(table_w_data), header=1, encoding='latin1')[0]
    
    # pega os nomes (headers) das colunas da tabela (.columns) e converte em uma lista (.tolist())
    dfheaders = df.columns.tolist()
    
    # roubei da net :)  remove os headers duplicados magicamente, n sei como funciona
    df1 = df[df.iloc[:, 0] != df.columns[0]]
    
    # iterando sobre as linhas do dataframe
    for (index, row) in df1.iterrows():
        
        # converte a linha da tabela em uma lista de valores
        row = row.array
        
        # inicializa um dicionario vazio
        dado = {}
        
        # itera sobre os elementos da linha, devolvendo tuplas (INDICE, VALOR) da lista
        for j, element in enumerate(row): # PARA CADA (numero do elemento & elemento) NA LINHA
            dado.update({dfheaders[j]: element}) # ADICIONA UMA NOVA CHAVE NO DICIONARIO, SENDO {listaDeHeaders[numeroDoElemento]: elementoDaLinha}
            
        dado = info['parser'](dado)
        # Adiciona o dicionário à lista de dados gerais
        dados_gerais.append(dado)
        # POSTA O DICIONARIO NO SERVIDOR
        print(dado)
        #sesh.post("http://localhost:8080/jogadores", json=dado)

# Cria um DataFrame com todos os dados coletados
#df_geral = pd.DataFrame(dados_gerais)

# Reordena as colunas do DataFrame
ordem_colunas = ["jogador", "nacionalidade", "posicao", "equipe", "idade", "nascimento", "indices"]
#df_geral = df_geral[ordem_colunas]

# Salva o DataFrame em um arquivo CSV
#df_geral.to_csv("dados_jogadoress.csv", index=False, encoding='utf-8')
