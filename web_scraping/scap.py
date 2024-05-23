# IMPORTACAO DE MODULOS
from bs4 import BeautifulSoup as bs # modulo para processar html
import pandas as pd # mexe com tabelas
import requests # acessa urls e extrai o codigo deles
import json # processa dicionarios em formato acessivel para sites ou progWeb
from parsers import *
from constantes import *


# LISTAS DE URLS E IDS DAS TABELAS
mapa_urls = {
    0: {
        "url": f"https://fbref.com/pt/comps/24/2023/stats/2023-Serie-A-estatisticas",
        "table_id": "stats_standard",
        "parser": payload_standard,
        "skip": True
    },
    1: {
        "url": "https://fbref.com/pt/comps/24/2023/passing/2023-Serie-A-estatisticas",
        "table_id": "stats_passing",
        "parser": payload_passing,
        "skip": True
    },
    2: {
        "url": "https://fbref.com/pt/comps/24/2023/keepersadv/2023-Serie-A-estatisticas",
        "table_id": "stats_keeper_adv",
        "parser": payload_keepersadv,
        "skip": True
    },
    3: {
        "url": "https://fbref.com/pt/comps/24/2023/shooting/2023-Serie-A-estatisticas",
        "table_id": "stats_shooting",
        "parser": payload_shooting,
        "skip": True
    },
    4: {
        "url": "https://fbref.com/pt/comps/24/2023/passing_types/2023-Serie-A-estatisticas",
        "table_id": "stats_passing_types",
        "parser": payload_passing_types,
        "skip": True
    },
    5: {
        "url": "https://fbref.com/pt/comps/24/2023/gca/2023-Serie-A-estatisticas",
        "table_id": "stats_gca",
        "parser": payload_gca,
        "skip": False
    },
    6: {
        "url": "https://fbref.com/pt/comps/24/2023/possession/2023-Serie-A-estatisticas",
        "table_id": "stats_possession",
    },
    7: {
        "url": "https://fbref.com/pt/comps/24/2023/playingtime/2023-Serie-A-estatisticas",
        "table_id": "stats_playing_time",
    },
    8: {
        "url": "https://fbref.com/pt/comps/24/2023/misc/2023-Serie-A-estatisticas",
        "table_id": "stats_misc",
    },
}

sesh = requests.Session() # inicializa uma sessao no modulo requests

for i, info in mapa_urls.items(): # itera sobre a lista de urls, devolve tuplas (INDICE, VALOR) da lista
    
    if 'parser' not in info or info['parser'] == None:
        print(f"{info['url']}: pulado")
        continue
    if 'skip' in info and info['skip']: continue
    
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
#    print(df)
    
    # roubei da net :)  remove os headers duplicados magicamente, n sei como funciona
    df1 = df[df.iloc[:, 0] != df.columns[0]]
    # print(dfheaders)
    
    # iterando sobre as linhas do dataframe
    for (index, row) in df1.iterrows():
        
        # converte a linha da tabela em uma lista de valores
        row = row.array
        
        # inicializa um dicionario vazio
        dado = {}
        
        # itera sobre os elementos da linha, devolvendo tuplas (INDICE, VALOR) da lista
        # PASSO A PASSO:
        for j, element in enumerate(row): # PARA CADA (numero do elemento & elemento) NA LINHA
            dado.update({dfheaders[j]: element}) # ADICIONA UMA NOVA CHAVE NO DICIONARIO, SENDO {listaDeHeaders[numeroDoElemento]: elementoDaLinha}
            
        dado = info['parser'](dado)
        # POSTA O DICIONARIO NO SERVIDOR
        print(dado)
       # sesh.post("http://localhost:8080/jogadores", json=dado)