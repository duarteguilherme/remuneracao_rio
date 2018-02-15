import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup


funcionarios = pd.read_json('funcionarios_id.json')
n_funcionarios = funcionarios.shape[0]


def baixa_id(id_funcionario):
    url = f'https://www.consultaremuneracao.rj.gov.br/ConsultaRemuneracao/vinculos/?id={id_funcionario}'    
    print(url)
    pagina = requests.get(url)
    parsed_page = BeautifulSoup(pagina.text, 'html.parser')
    dados = {}
    dados['id_funcionario'] = id_funcionario
    try:
        dados['cargo'] = ','.join([ x.text for x in parsed_page.find('div', attrs={'class':"collapsible-header blue-grey darken-4 white-text" }).find_all('span') ])
    except:
        dados['cargo'] = ''
    try:
        dados['matricula'] = '-'.join([x.text for x in parsed_page.find('table', attrs={'class':"responsive-table striped highlight bordered" }).find_all('td') ])
    except:
        dados['matricula'] = ''
    try:
        dados['link_remuneracao'] = [ x['href'] for x in parsed_page.find_all('a') if 'ConsultaRemuneracao' in x['href'] ][1]
    except:
        dados['link_remuneracao'] = 'nao_encontrado'
    return(dados)

for i in range(int(sys.argv[1]), int(sys.argv[2])):
    print(i)
    print(funcionarios.iloc[i])
    with open('dados_vinculo.csv','a') as f:
        (pd.DataFrame({ **(funcionarios.iloc[i].to_dict()), **(baixa_id(funcionarios.iloc[i].cpfEncode))}, index=[0])).to_csv(f, index=None, header=None)


