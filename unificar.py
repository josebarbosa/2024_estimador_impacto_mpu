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
#pd.read_excel("the_document.ods", engine="odf")
print("Aguarde... carregando Dataframes")
print("MPDFT")
mpdft_pensionistas = pd.read_excel('anexos/mpdft_valores_pensionistas_marco_2024.ods', engine='odf')
mpdft_ativo = pd.read_excel('anexos/mpdft_remuneracao_servidores_ativos_marco_2024.ods', engine='odf')
mpdft_inativo = pd.read_excel('anexos/mpdft_proventos_servidores_inativos_marco_2024.ods', engine='odf') 
print("MPF")
mpf_ativo = pd.read_excel('anexos/remuneracao-servidores-ativos_2024_Marco.ods', engine='odf')
mpf_inativo = pd.read_excel('anexos/provento-servidores-inativos_2024_Marco.ods', engine='odf')
mpf_pensionista = pd.read_excel('anexos/valores-percebidos-pensionistas_2024_Marco.ods', engine='odf')
print("MPM")
mpm_ativo = pd.read_excel('anexos/mpm_remuneracao_servidores_ativos_marco_2024.ods', engine='odf')
mpm_inativo = pd.read_excel('anexos/mpm_proventos_servidores_inativos_marco_2024.ods', engine='odf')
mpm_pensionista = pd.read_excel('anexos/mpm_valores_pensionistas_marco_2024.ods', engine='odf')
print("MPT")
mpt_ativo = pd.read_excel('anexos/mpt_remuneracao_servidores_ativos_marco_2024.ods', engine='odf')
mpt_inativo = pd.read_excel('anexos/mpt_proventos_servidores_inativos_marco_2024.ods', engine='odf')
mpt_pensionista = pd.read_excel('anexos/mpt_valores_pensionistas_marco_2024.ods', engine='odf')
print("Conclusão da carga de Dataframes")

#apensar a coluna de situação funcional (ativo, inativo ou pensionista) a cada um dos dataframes
mpdft_ativo['situacao_funcional'] = 'ativo'
mpdft_inativo['situacao_funcional'] = 'inativo'
mpdft_pensionistas['situacao_funcional'] = 'pensionista'
mpf_ativo['situacao_funcional'] = 'ativo'
mpf_inativo['situacao_funcional'] = 'inativo'
mpf_pensionista['situacao_funcional'] = 'pensionista'
mpm_ativo['situacao_funcional'] = 'ativo'
mpm_inativo['situacao_funcional'] = 'inativo'
mpm_pensionista['situacao_funcional'] = 'pensionista'
mpt_ativo['situacao_funcional'] = 'ativo'
mpt_inativo['situacao_funcional'] = 'inativo'
mpt_pensionista['situacao_funcional'] = 'pensionista'

#unificar dataframe por ramo
print("Concatenando MPDFT")
mpdft = pd.concat([mpdft_ativo, mpdft_inativo, mpdft_pensionistas])
mpdft.info()
print("Concatenando MPF")
mpf = pd.concat([mpf_ativo, mpf_inativo, mpf_pensionista])
mpf.info()
print("Concatenando MPM")
mpm = pd.concat([mpm_ativo, mpm_inativo, mpm_pensionista])
mpm.info()
print("Concatenando MPT")
mpt = pd.concat([mpt_ativo, mpt_inativo, mpt_pensionista])
mpt.info()

# TODO - fazer tratamento dos dados


# TODO - transformar o dataframe num CSV a ser lido pelo arquivo principal