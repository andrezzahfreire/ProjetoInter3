from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd

url = "https://fbref.com/pt/comps/24/2023/stats/2023-Serie-A-estatisticas"


driver = webdriver.Chrome()

driver.get(url)

html_content = driver.page_source

soup = BeautifulSoup(html_content, "html.parser")

driver.quit()


table = soup.find("table", id="stats_standard")
df = pd.read_html(str(table), decimal=',', thousands='.')[0]
print(df)

