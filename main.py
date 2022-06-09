from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pandas as pd


def WebScrapping(url):
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='wikitable sortable')

    A = []
    B = []
    C = []
    D = []
    E = []

    for row in table.findAll('tr'):
        cells = row.findAll('td')
        if len(cells) == 5:
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find('a').text)
            E.append(cells[4].find(text=True))

    df = pd.DataFrame(index=A, columns=['Posição'])

    df['Posição'] = A
    df['Estado'] = B
    df['Código/IBGE'] = C
    df['Capital'] = D
    df['Área'] = E


    result = df.to_html()

    text_file = open("index.html", "w")
    text_file.write(result)
    text_file.close()



# teste webscrapping only para criar relatorio agrupoado por nomes
##
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    WebScrapping('https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
