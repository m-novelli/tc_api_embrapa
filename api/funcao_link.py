import requests
from bs4 import BeautifulSoup
import pandas as pd
from flask import jsonify

def webscrap (url):

    # Faz uma requisição GET para a URL fornecida
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    response.raise_for_status()

    # Parseia o HTML da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra a tabela específica com a classe 'tb_base tb_dados'
    table = soup.find('table', {'class': 'tb_base tb_dados'})


    # Extrai as linhas da tabela
    rows = table.find_all('tr')

    # Lista para armazenar os dados
    data = []

    # Itera sobre as linhas e extrai o texto das células (td)
    for row in rows:
        cells = row.find_all(['th', 'td'])  # Inclui cabeçalhos (th) e dados (td)
        cells_text = [cell.get_text(strip=True) for cell in cells]
        data.append(cells_text)

    # Converte os dados em um DataFrame do pandas
    df = pd.DataFrame(data)

    df = pd.DataFrame(data[1:], columns=data[0])


    return df


        
webscrap('http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_02')

def webscrap_title(url):

    # Faz uma requisição GET para a URL fornecida
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    response.raise_for_status()

    # Parseia o HTML da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra o título da página
    title = soup.title.string

    return title