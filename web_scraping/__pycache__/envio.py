import pandas as pd
import requests

# Caminho correto para o arquivo CSV
csv_path = 'C:/Users/felipe.botelho/Documents/GitHub/ProjetoInter3/web_scraping/dados_jogadores.csv'

# Lê o arquivo CSV
df = pd.read_csv(csv_path)

# Exemplo de envio dos dados para o Spring Boot
url = 'http://localhost:8080/jogadores'  # Substitua pela URL correta do seu endpoint

# Itera sobre os jogadores e envia cada um como um objeto JSON separado
for index, jogador in df.iterrows():
    # Converte o jogador para um formato que pode ser enviado
    data = {
        "jogador": jogador["jogador"],
        "nacionalidade": jogador["nacionalidade"],
        "posicao": jogador["posicao"],
        "equipe": jogador["equipe"],
        "idade": int(jogador["idade"]),
        "nascimento": int(jogador["nascimento"]),
        "indices": eval(jogador["indices"])  # Avalia a string para transformar em um dicionário Python
    }
    
    # Faz a requisição POST com os dados formatados corretamente
    response = requests.post(url, json=data)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        print(f'Dados do jogador {index} enviados com sucesso para o Spring Boot!')
    else:
        print(f'Erro ao enviar os dados do jogador {index} para o Spring Boot. Status code: {response.status_code}')
        print(response.text)
