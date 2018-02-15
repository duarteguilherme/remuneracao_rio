import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import json

funcionarios = (pd.read_csv('dados_vinculo.csv', header=None))
funcionarios.columns =  ['cargo', 'cpfEncode', 'cpfMask', 'cpfEncode2', 'link_remuneracao', 'matricula', 'nome']
n_funcionarios = funcionarios.shape[0]


#def baixa_salario(cargo, cpfEncode, cpfMask, cpfEncode2, link_remuneracao, matricula, nome):
def baixa_salario(linha):
    url = 'https://www.consultaremuneracao.rj.gov.br' + linha['link_remuneracao']
    pagina = requests.get(url)
    parsed_page = BeautifulSoup(pagina.text, 'html.parser')
    tabela = parsed_page.find('table', attrs={'class':"responsive-table striped highlight bordered table-lista-mes"})
    trs = tabela.find_all('tr')
    dados = linha
    for i in trs:
        if i.find('th') is not None:
            continue
        else:
            dados[i.find_all('td')[0].text.strip()] = i.find_all('td')[1].text.strip()
    return(dados)


for i in range(int(sys.argv[1]), int(sys.argv[2])):
    print(i)
    base = json.dumps(baixa_salario((funcionarios.iloc[i].to_dict())))
    with open('dados_remuneracao.json','a') as f:
        f.write(base)
        f.write('\n')


