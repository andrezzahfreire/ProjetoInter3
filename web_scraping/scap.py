# IMPORTACAO DE MODULOS
from bs4 import BeautifulSoup as bs # modulo para processar html
import pandas as pd # mexe com tabelas
import requests # acessa urls e extrai o codigo deles
import json # processa dicionarios em formato acessivel para sites ou progWeb

# LISTAS DE URLS E IDS DAS TABELAS
urls = ["https://fbref.com/pt/comps/24/2023/stats/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/passing/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/keepersadv/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/shooting/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/passing/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/passing_types/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/gca/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/possession/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/playingtime/2023-Serie-A-estatisticas", 
        "https://fbref.com/pt/comps/24/2023/misc/2023-Serie-A-estatisticas"]

table_ids = ["stats_standard", 
             "stats_passing", 
             "stats_keeper_adv", 
             "stats_shooting", 
             "stats_passing", 
             "stats_passing_types", 
             "stats_gca", 
             "stats_possession", 
             "stats_playing_time", 
             "stats_misc"]

sesh = requests.Session() # inicializa uma sessao no modulo requests

for i, url in enumerate(urls): # itera sobre a lista de urls, devolve tuplas (INDICE, VALOR) da lista
    
    # pega o codigo html da url e remove marcadores de comentarios, transformando todo comentario em 'parte do codigo' <-- A TABELA TAVA ESCONDIDA NOS COMENTARIOS    
    response = requests.get(url).text.replace('<!--', '').replace('-->', '')
    
    # transforma o codigo html em um objeto BeautifulSoup, que permite a busca de elementos html
    soup = bs(response, 'html.parser')
    
    # no objeto BS, procura a tabela com o id especificado na lista de ids com o mesmo indice do URL
    table_w_data = soup.select_one(f'table#{table_ids[i]}')
    
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
        # PASSO A PASSO:
        for j, element in enumerate(row): # PARA CADA (numero do elemento & elemento) NA LINHA
            dado.update({dfheaders[j]: element}) # ADICIONA UMA NOVA CHAVE NO DICIONARIO, SENDO {listaDeHeaders[numeroDoElemento]: elementoDaLinha}
            
        dado = {
            "Class.": int(dado["Class."]),
            "Jogador": "Bruno Zapelli",
            "Nação": "ar ARG",
            "Pos.": "LT,AT",
            "Equipe": "Ath Paranaense",
            "Idade": int(dado["Idade"]),
            "Nascimento": int(dado["Idade"]),
            "indices": {
                "MP": 21,
                "Inícios": 13,
                "Min.": "1.143",
                "90s": "12.7",
                "Gols": "2",
                "Assis.": "2",
                "G+A": "4",
                "G-PB": "2",
                "PB": "0",
                "PT": "0",
                "CrtsA": "0",
                "CrtV": "0",
                "xG": "2.5",
                "npxG": "2.5",
                "xAG": "1.8",
                "npxG+xAG": "43",
                "PrgC": "35",
                "PrgP": "72",
                "PrgR": "71",
                "Gols.1": "016",
                "Assis..1": "016",
                "G+A.1": "031",
                "G-PB.1": "016",
                "G+A-PB": "031",
                "xG.1": "019",
                "xAG.1": "014",
                "xG+xAG": "034",
                "npxG.1": "019",
                "npxG+xAG.1": "034",
            },
            "Partidas": "Partidas",
        }

        print(json.dumps(dado, ensure_ascii=False))
        # POSTA O DICIONARIO NO SERVIDOR
        #sesh.post("http://localhost:8080/jogadores", json=json.dumps(dado))
        
        
