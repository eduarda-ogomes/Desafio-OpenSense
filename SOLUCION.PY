from bs4 import BeautifulSoup 
import pandas as pd
import re

#caminho dos arquivos
arquivos = [
    'arquivos html/arquivo01.html',
    'arquivos html/arquivo02.html',
    'arquivos html/arquivo03.html',
    'arquivos html/arquivo04.html',
    'arquivos html/arquivo05.html',
    'arquivos html/arquivo06.html',
    'arquivos html/arquivo07.html',
    'arquivos html/arquivo08.html',
    'arquivos html/arquivo09.html',
    'arquivos html/arquivo10.html'
]

#variavel pra guardar os processos encontrado em cada arquivo
todos_processos = []

#ler os arquivos disponibilizados
for caminho_arquivo in arquivos:
    with open(caminho_arquivo, 'r', encoding='latin-1') as arquivo:
        dados_pagina = BeautifulSoup(arquivo, 'html.parser')

    #nome do arquivo que esta sendo analisado
    nome_arquivo = caminho_arquivo.split('/')[-1]
    
    #filtrar os cnpj do arquivo
    encontrar_cnpj = dados_pagina.find(string= re.compile("CPF ou CNPJ"))
    cnpj = re.search(r'\d{14}', encontrar_cnpj).group()

    #encontrando os processos e suas informações
    processos = []
    linhas = dados_pagina.find_all('tr', bgcolor=True)
    
    #calcular quantos processos existem em cada arquivo
    quantidade_processos = 0
    for linha in linhas:
        colunas = linha.find_all('td')
        if len(colunas)>= 4:
            quantidade_processos += 1

    #variavel se encontrou ou nao processo no arquivo
    processos_encontrados = False

    #loop pra analisar todos as linhas e colunas da tabela
    for linha in linhas:
        colunas = linha.find_all('td')
        if len(colunas) >= 4:
            processo = {
                'Arquivo': nome_arquivo,
                'CNPJ': cnpj,
                'Resultado': quantidade_processos,
                'Número do pedido': colunas[0].get_text().strip(),
                'Data do Depósito': colunas[1].get_text().strip(),
                'Título': colunas[2].get_text().strip(),
                'IPC': colunas[3].get_text().strip()
            }
            todos_processos.append(processo)
            processos_encontrados = True

    #se não encontrou processo no documento executa 
    if not processos_encontrados:
        processo_vazio = {
            'Arquivo': nome_arquivo,
            'CNPJ': cnpj,
            'Resultado': 0,
            'Número do pedido': '-',
            'Data do Depósito': '-',
            'Título': '-',
            'IPC': '-'
        }
        todos_processos.append(processo_vazio)

print(todos_processos)


#criando um arquivo html com o pandas
df = pd.DataFrame(todos_processos)
html = df.to_html(index=False)

#redimensionando a tabela com css
html = f"""
<style>
table {{
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed; 
}}

th, td {{
    border: 1px solid black;
    padding: 6px;
    word-wrap: break-word; 
    white-space: normal;
}}
</style>
{html}
"""

#salvando alterações no arquivo html
with open('PATENTES.html', 'w', encoding='utf-8') as f:
    f.write(html)

