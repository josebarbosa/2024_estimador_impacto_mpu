# 2024_estimador_impacto_mpu

# Projeto de cálculo de impacto orçamentário de reajustes do MPU
Este projeto visa unificar os dados de servidores de todos os ramos do MPU (MPF, MPT, MPM e MPDFT) e estimar impactos orçamentários decorrentes de eventuais planos de carreira. 

## Modelo de algoritmo
Para alcançar o objetivo pretendido, os dados de diferentes bases devem ser unificados, e criados algoritmos que tentem identificar exatamente a composição das remunerações e proventos dos servidores, uma vez que a granularidade disponibilizada pelas bases, via de regra, é insuficiente para precisar com clareza a situação funcional do servidor, em termos de, entre outros, posicionamento na carreira, gratificações recebidas, eventual margem de evolução, ou rubricas coincidentes. 

## Bases de dados utilizadas
Para este estudo, são utilizadas as seguintes bases de dados:

Para definição de estimativa de custos: 
http://www.transparencia.mpf.mp.br/conteudo/gestao-de-pessoas/tabelas-portaria-sof-segep/2024/anexo_II_servidores_2024_pdf.pdf
http://www.transparencia.mpf.mp.br/conteudo/gestao-de-pessoas/tabelas-portaria-sof-segep/2024/anexo_III_2024_pdf.pdf

Remuneração de servidores ativos:
http://www.transparencia.mpf.mp.br/conteudo/contracheque/remuneracao-servidores-ativos

Proventos de inativos: 
http://www.transparencia.mpf.mp.br/conteudo/contracheque/provento-servidores-inativos

Valores recebidos de pensionistas:
http://www.transparencia.mpf.mp.br/conteudo/contracheque/valores-percebidos-pensionistas

Quadro de servidores ativos e inativos do MPF:
http://www.transparencia.mpf.mp.br/conteudo/gestao-de-pessoas/quadro-de-servidores

Quadro de pensionistas do MPF:
http://www.transparencia.mpf.mp.br/conteudo/gestao-de-pessoas/pensionista

Remuneração dos servidores ativos do MPT:
https://mpt.mp.br/MPTransparencia/pages/portal/remuneracaoServidoresAtivos.xhtml

Proventos dos servidores inativos do MPT:
https://mpt.mp.br/MPTransparencia/pages/portal/proventosServidoresInativos.xhtml

Valores recebidos por pensionistas do MPT:
https://mpt.mp.br/MPTransparencia/pages/portal/proventosPensionistas.xhtml

Quadro de servidores ativos e inativos do MPT:

https://mpt.mp.br/MPTransparencia/pages/portal/servidoresAtivos.xhtml

https://mpt.mp.br/MPTransparencia/pages/portal/servidoresInativos.xhtml

Quadro de pensionistas do MPT:
https://mpt.mp.br/MPTransparencia/pages/portal/pensionistas.xhtml

Contracheques do MPM:
https://transparencia.mpm.mp.br/contracheque/

Remuneração dos servidores ativos do MPDFT:
https://www.mpdft.mp.br/transparencia/index.php?item=remuneracao&tipo=servidoresAtivos&resp=REMUNERACAO&titulo=Remunera%C3%A7%C3%A3o%20de%20todos%20os%20servidores%20ativos

Proventos dos servidores inativos do MPDFT
https://www.mpdft.mp.br/transparencia/index.php?item=remuneracao&tipo=servidoresInativos&resp=REMUNERACAO&titulo=Proventos%20de%20todos%20os%20servidores%20inativos

Valores recebidos por pensionistas do MPDFT
https://www.mpdft.mp.br/transparencia/index.php?item=remuneracao&tipo=pensionistas&resp=REMUNERACAO&titulo=Valores%20percebidos%20por%20todos%20os%20pensionistas


## Peculiaridades

Para servidores inativos e pensionistas, é preciso detectar se o regime é de paridade ou não. O impacto deve se restringir àquela opção, enquanto os benefícios decorrentes de média possuem metodologia própria de correção, baseada no INPC e aplicada anualmente em janeiro. 

A análise será obtida a partir da competência **março/2024**. Isto porque os estudos orçamentários e a elaboração do Projeto de Lei de Diretrizes orçamentárias tomam esta competência como base para apurar os quantitativos e despesas relacionadas aos gastos com servidores. 