import requests
from bs4 import BeautifulSoup
import json

data_post = {
"draw":"1",
"columns[0].data":"nome",
"columns[0].name":"",
"columns[0].searchable":"true",
"columns[0].orderable":"false",
"columns[0].search.value":"",
"columns[0].search.regex":"false",
"columns[1].data":"cpfMask",
"columns[1].name":"",
"columns[1].searchable":"true",
"columns[1].orderable":"false",
"columns[1].search.value":"",
"columns[1].search.regex":"false",
"columns[2].data":"cpfEncode",
"columns[2].name":"",
"columns[2].searchable":"true",
"columns[2].orderable":"false",
"columns[2].search.value":"",
"columns[2].search.regex":"false",
"order[0].column":"0",
"order[0].dir":"asc",
"start":"0",
"length":"1000000",
"search.value":"",
"search.regex":"false",
"nome":"",
"id":""
}

url = "https://www.consultaremuneracao.rj.gov.br/ConsultaRemuneracao/api/servidores/data"
pagina = requests.post(url, data = data_post, verify=False)
dados_funcionarios = json.loads(pagina.text)['data']
dados_funcionarios = json.dumps(dados_funcionarios)

print(data_post)

with open('funcionarios_id.json','a') as f:
    f.write(dados_funcionarios)
