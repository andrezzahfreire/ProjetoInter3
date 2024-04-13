from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import variaveis as v


url = v.url
id = v.id_table
df = pd.DataFrame()
for site in url :
    # index = str(url.index(site))
    driver = webdriver.Chrome()

    driver.get(site)

    html_content = driver.page_source

    soup = BeautifulSoup(html_content, "html.parser")

    driver.quit()

    table = soup.find("table", id= id[url.index(site)])
    df = pd.concat([df, pd.read_html(str(table), decimal=',', thousands='.')[0]], ignore_index=True)
    
    
df.to_csv('dados_jogadores.csv', index=False)
    
    

