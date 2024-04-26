from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import variaveis as v
import requests as req
import json


url = v.url
id = v.id_table
df = pd.DataFrame()
for site in url :
    index = str(url.index(site))
    driver = webdriver.Chrome()

    driver.get(site)

    html_content = driver.page_source

    html_content = html_content.replace('>Pos.<', '>Posicao<')
    soup = BeautifulSoup( html_content, "html.parser")

    driver.quit()

    table = soup.find("table", id= id[url.index(site)])
    df = pd.concat([df, pd.read_html(str(table), decimal=',', thousands='.', header=1)[0]], ignore_index=True)
    df = df.loc[df['Class.'] != 'Class.']
    df.to_csv('scrap.csv', index=False)
    
    headers = {
        'Content-type': 'application/json'
    }
    session = req.Session()
    for (index, row) in df.iterrows():
        print(row)
        dado = {
            "jogador": row['Jogador'],  
            "nacionalidade": row['Nação'],
            "posicao": row['Posicao'],  
            "equipe": row['Equipe'], 
            "idade": row['Idade'], 
            "nascimento": row['Nascimento'],
            "jogosDisputados": row['MP'], # Jogos disputados
            "inicios": row['Inícios'],  
            "minutos": row['Min.'],   # Jogos disputados
            "90s": row['90s'],        # 90 minutos jogados
            "gols": row['Gols'],      # Gols marcados
            "assistencias": row['Assis.'],  # Assistências
            "gols_assistencias": row['G+A'],  # Gols + Assistências
            "gols_penal": row['G-PB'],       # Gols de pênalti
            "penaltis_batidos": row['PB'],   # Pênaltis batidos
            "passes_tentados": row['PT'],    # Passes tentados
            "cartoes_amarelos": row['CrtsA'],  # Cartões amarelos
            "cartoes_vermelhos": row['CrtV'],  # Cartões vermelhos
            "xG": row['xG'],         # Expected Goals (Gols esperados)
            "npxG": row['npxG'],     # Non-penalty Expected Goals (Gols esperados sem pênaltis)
            "xAG": row['xAG'],       # Expected Assists (Assistências esperadas)
            "goleassis": row['npxG+xAG'],  # Expected Goals + Expected Assists (Gols esperados + Assistências esperadas)
            "progressao_carregada": row['PrgC'],   # Progressão carregada
            "progressao_passada": row['PrgP'],    # Progressão passada
            "progressao_recebida": row['PrgR'],   # Progressão recebida
        }
        session.post(
            "http://localhost:8080/jogadores", json=json.dumps(dado)
        )
        print(dado)
    
    