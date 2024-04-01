from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://fbref.com/pt/comps/24/2023/stats/2023-Serie-A-estatisticas"


driver = webdriver.Chrome()

driver.get(url)


html_content = driver.page_source

soup = BeautifulSoup(html_content, "html.parser")


table = soup.find("table", id="stats_standard") 


if table:

  table_rows = table.find_all("tr")

  
  extracted_data = []
  
  for row in table_rows:
    row_data = []  
    
    data_cells = row.find_all("td")
    
    for cell in data_cells:
      cell_text = cell.text.strip()  
      row_data.append(cell_text)
    extracted_data.append(row_data)

  print(extracted_data)
 
else:
  print("Table not found!")

# Close the browser window
driver.quit()
