'''
Aplicação desenvolvida por José Antonio dos Santos Barbosa
contato: jose@josebarbosa.com.br
Arquivo responsável por unificar as remunerações, proventos e valores recebidos pelos servidores, inativos e pensionistas de todos os ramos. 
O resultado final deve ser um dataframe padronizado que, além das colunas disponíveis no portal da transparência, deve considerar a situação de regime previdenciário, já que esta rubrica e a respectiva contribuição patronal variam de acordo com o regime
'''

import pandas as pd 

# TODO - avaliar se vai precisar utilizar este recurso
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#pd.set_option('display.width', 1000)
#pd.set_option('max_columns', None)

# TODO - carregar tabelas de cada um dos ramos
# São 3 tabelas de cada: remunerações, proventos e valores recebidos (respectivamente de servidores ativos, servidores inativos e pensionistas)


# TODO - fazer tratamento dos dados

# TODO - transformar o dataframe num CSV a ser lido pelo arquivo principal