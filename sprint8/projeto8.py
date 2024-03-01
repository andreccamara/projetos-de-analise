#!/usr/bin/env python
# coding: utf-8

# # Sumário 
# <a id='sumário'></a>
# 
# - [Sumário](#sumário)
#   - [Seção 1: Análise prévia](#seção-1)
#     - [Subseção 1.1. Carregamento de dados](#subsecao-11-carregamento-de-dados)
#     - [Subseção 1.2. Análise de prioridade de hipóteses](#subseção-12-análise-de-prioridade-de-hipóteses)
#     - [Subseção 1.3. Conclusões](#subseção-13-conclusões)
#   - [Seção 2: Análise de dados](#seção-2-análise-de-dados)
#     - [Subseção 2.1. Limpeza de dados](#subseção-21-limpeza-de-dados)
#     - [Subseção 2.2. Tarefa 1: Gráfico da receita acumulada por grupo](#subseção-22-tarefa-1-gráfico-da-receita-acumulada-por-grupo)
#     - [Subseção 2.3. Tarefa 2: Gráfico do tamanho médio acumulado do pedido por grupo](#subseção-23)
#     - [Subseção 2.4. Tarefa 3: Gráfico da diferença relativa no tamanho médio acumulado do pedido para o grupo B em comparação com o grupo A](#seção-24)
#     - [Subseção 2.5. Tarefa 4: Taxa de conversão diária e diferença relativa na conversão cumulativa](#subseção-25)
#     - [Subseção 2.6. Tarefa 5: Identificação de anomalias nos dados](#subseção-26-tarefa-5-identificação-de-anomalias-nos-dados)
#     - [Subseção 2.7. Tarefa 6: Teste de significância estatística](#subseção-27-tarefa-6-teste-de-significância-estatística)
#     - [Subseção 2.8. Tarefa 7: Tomada de decisão](#seção-28)
#   - [Seção 3: Conclusões Gerais](#seção-3-conclusões-gerais)
# 

# - [Sumário](#sumário)
# ##   Análise Prévia
# 
# <a id='seção-1'></a>

# ### Carregamento de dados 
# <a id= 'subsecao-11-carregamento-de-dados'> </a>
# Esta seção carrega os dados de vendas de um arquivo CSV 
# 

# In[1]:


import pandas as pd
import numpy as np
import math as mth
from scipy import stats as st
import scipy.stats as stats
import datetime as dt
import matplotlib.pyplot as plt


# In[2]:


caminhoh='hypotheses_us.csv'
try:
    hipoteses=pd.read_csv('/datasets/hypotheses_us.csv', sep=';')
except:
    hipoteses=pd.read_csv(caminhoh, sep=';')


# In[3]:


hipoteses['Hypothesis']


# In[4]:


hipoteses.info()


# In[5]:


hipoteses[['Reach','Impact','Confidence','Effort']]


# ###  Análise de prioridade de hipóteses 
# <a class="" id='subseção-12-análise-de-prioridade-de-hipóteses'></a>
# 
# 

# 
# <font color='blue'> esta seção analisa qual hipotese seria mais benéfica de se priorisar segundo aplicação dos calculos de ICE e RICE
# 

# In[6]:


#RICE = Reach*Impact * Confidence /Effort
#ICE = Impact * Confidence /Effort
hipoteses['ICE']=hipoteses['Impact']*hipoteses['Confidence']/hipoteses['Effort']
hipoteses['RICE']=hipoteses['Impact']*hipoteses['Reach']*hipoteses['Confidence']/hipoteses['Effort']    
print(hipoteses.sort_values(by='RICE')[['Hypothesis','RICE']])
print(hipoteses.sort_values(by='ICE')[['Hypothesis','ICE']])


# In[7]:


#atribui-se IDs às hipoteses para melhor trabalhar a análise 
hipoteses['Hypothesis']= np.arange(9)+1


# In[8]:


hipoteses.sort_values(by='ICE', ascending=False)


# In[9]:


hipoteses.sort_values(by='RICE',ascending=False)


# ###  Conclusões <a class="" id='subseção-13-conclusões'></a>
# 
# 

# <font color="green">como percebemos, as hipoteses 8 , 3 e 1* são as melhores quando avaliamos o RICE.  
# Por outro lado, se formos avaliar apenas o ICE, agora são as hipoteses 9, 1 e 8* que se destacam.  
# Tudo isso nos revela que o alcance (reach) (que é a unica variavel responsavel pela diferença) varia significativamente.  
# Isso influencia positivamente as hipoteses 8 e 3, que ganham posições.  
# Entretando o alcance da 1ª e da 9ª hipotese são bem mais baixas comparativamente. </font>
# 
# 
# <details>
# <summary>
#     <b>*as hipoteses são as seguintes ↓</b>
# </summary>
# <font color="gray">
#     
# 1-Add two new channels for attracting traffic. This will bring 30% more users
# 
# 2-Launch your own delivery service. This will shorten delivery time
# 
# 3-Add product recommendation blocks to the store's site. This will increase conversion and average purchase size
# 
# 4-Change the category structure. This will increase conversion since users will find the products they want more quickly
# 
# 5-Change the background color on the main page. This will increase user engagement
# 
# 6-Add a customer review page. This will increase the number of orders
# 
# 7-Show banners with current offers and sales on the main page. This will boost conversion
# 
# 8-Add a subscription form to all the main pages. This will help you compile a mailing list
# 
# 9-Launch a promotion that gives users discounts on their birthdays
#     
# </font>
# </details>
# 
# 
# <details>
#     <summary>
#     <b>**em português ↓ </b>
# </summary>
# 
# 
# <font color="green">
#     
# 1-Adicione dois novos canais para atrair tráfego. Isso trará 30% mais usuários
# 
# 2-Lance seu próprio serviço de delivery. Isso reduzirá o tempo de entrega
# 
# 3-Adicione blocos de recomendação de produtos ao site da loja. Isso aumentará a conversão e o tamanho médio da compra
# 
# 4-Altere a estrutura da categoria. Isso aumentará a conversão, pois os usuários encontrarão os produtos que desejam mais rapidamente
# 
# 5-Altere a cor de fundo da página principal. Isso aumentará o envolvimento do usuário
# 
# 6-Adicione uma página de avaliação do cliente. Isso aumentará o número de pedidos
# 
# 7-Mostre banners com ofertas e promoções atuais na página principal. Isso aumentará a conversão
# 
# 8-Adicione um formulário de inscrição a todas as páginas principais. Isso ajudará você a compilar uma lista de discussão
# 
# 9-Lance uma promoção que dê descontos aos usuários em seus aniversários</font>
# </details>

# - [Sumário](#sumário)
# ## Análise de dados 
# <a class="" id='seção-2-análise-de-dados'></a>
# 
# 

# In[10]:


caminhop='orders_us.csv'
try:
    pedidos=pd.read_csv('/datasets/orders_us.csv')
except:
    pedidos=pd.read_csv(caminhop)


# In[11]:


caminhov='visits_us.csv'
try:
    visitas=pd.read_csv('/datasets/visits_us.csv')
except:
    visitas=pd.read_csv(caminhov)
    


# - [Sumário](#sumário)
# ###  Limpeza de dados 
# <a class="" id='subseção-21-limpeza-de-dados'></a>
# 
# 

# In[12]:


#tirando duplicadas e passando para datetime
pedidos=pedidos.drop_duplicates()
visitas = visitas.drop_duplicates()


# In[13]:


visitas.info()


# In[14]:


visitas['date'] = pd.to_datetime(visitas['date'])


# In[15]:


pedidos.info()
pedidos['date'] = pd.to_datetime(pedidos['date'])


# <font color='gray'> alguns clientes participaram tanto do grupo A, quanto do B, temos que retirá-los da análise para não haver contaminação</font>

# In[16]:


idsA=pedidos[pedidos['group']=='A']
idsB=pedidos[pedidos['group']=='B']
pedidosduplosA=idsA[idsA['visitorId'].isin(idsB['visitorId'])]
pedidosduplosB=idsB[idsB['visitorId'].isin(idsA['visitorId'])]


# In[17]:


pedidosduplos=pd.concat([pedidosduplosA, pedidosduplosB])
pedidosduplos.sort_values(by='visitorId')


# In[18]:


pedidoslimpo = pedidos[~pedidos['visitorId'].isin(pedidosduplos['visitorId'])].reset_index()
pedidoslimpo


# <font color='gray'> agora calculamos quantas visitas e pedidos houve, com o passar dos dias, de forma acumulad .
# para tanto, aplicamos nunique() aos visitantes(visitorId)e às compras(transactionId) bem como sum() à receita(revenue), conforme se ve:.

# In[19]:


visitasAcumulada = pedidoslimpo.apply(lambda x: visitas[np.logical_and(visitas['date'] <= x['date'], visitas['group'] == x['group'])].agg({'date' : 'max', 'group' : 'max', 'visits' : 'sum'}), axis=1).sort_values(by=['date','group'])
visitasAcumulada=visitasAcumulada.drop_duplicates()


# In[20]:


comprasAcumulada=pedidoslimpo.apply(lambda x: pedidoslimpo[np.logical_and(pedidoslimpo['date'] <= x['date'], pedidoslimpo['group'] == x['group'])].agg({'date' : 'max', 'group' : 'max', 'transactionId' : pd.Series.nunique, 'visitorId' : pd.Series.nunique, 'revenue' : 'sum'}), axis=1).sort_values(by=['date','group'])
comprasAcumulada=comprasAcumulada.drop_duplicates()


# In[21]:


visitasAcumulada.columns


# In[22]:


comprasAcumulada.columns


# agora que temos os dados das compras e das visitas, será comodo juntá-los em uma mesma tabela:

# In[23]:


dadosAcumulados = comprasAcumulada.merge(visitasAcumulada, left_on=['date', 'group'], right_on=['date', 'group'])
dadosAcumulados.columns = ['date', 'group', 'orders', 'buyers', 'revenue', 'visitors']
dadosAcumulados


# ###  Tarefa 1: Gráfico da receita acumulada por grupo <a class="" id='subseção-22-tarefa-1-gráfico-da-receita-acumulada-por-grupo'></a>
# 

# <font color='blue'>1. Vamos fazer um gráfico da receita acumulada por grupo. 

# In[25]:


comprasAcumulada


# temos que separar os dados por grupo, depois plotar em grafico

# In[26]:


comprasAcumuladaA=comprasAcumulada[comprasAcumulada['group']=='A']


# In[27]:


comprasAcumuladaB=comprasAcumulada[comprasAcumulada['group']=='B']


# In[28]:


plt.figure(figsize=(16, 9))
plt.plot(comprasAcumuladaA['date'], comprasAcumuladaA['revenue'], label='A')
plt.plot(comprasAcumuladaB['date'], comprasAcumuladaB['revenue'], label='B')
plt.legend()
plt.figure()



# <font color='blue'> 2. conclusões e conjecturas.

# <font color='green'>concluo que o grupo B apresentou visivelmente mais resultado, porem pode ser devido a uma grande flutuação do dia 18, causada por outliers 

# 
# ### Subseção 2.3: Tarefa 2: Gráfico do tamanho médio(da compra) acumulado do pedido por grupo 
# <a class="" id='subseção-23'></a>
# 
# 

# <font color='blue'>1. Fazer um gráfico do tamanho médio acumulado do pedido por grupo. 

# In[30]:


plt.figure(figsize=(16,8))
plt.plot(comprasAcumuladaA['date'], comprasAcumuladaA['revenue']/comprasAcumuladaA['transactionId'], label='A')
plt.plot(comprasAcumuladaB['date'], comprasAcumuladaB['revenue']/comprasAcumuladaB['transactionId'], label='B')
plt.legend()
plt.figure()


# <font color='blue'>2.  conclusões e conjecturas.

# <font color='green'>percebe-se que, de fato, a grande diferença de receita total se deve a abrupta alta de valor medio de vendas no dia 18 de ago, o que provavelmente se deve a outliers, é o que se investigará!

# ### Subseção 2.4: Tarefa 3: Gráfico da diferença relativa no tamanho médio acumulado do pedido para o grupo B em comparação com o grupo A 
# <a class="" id='seção-24'></a>
# 
# 

# 
# <font color='blue'>1. Fazer um gráfico da diferença relativa no tamanho médio acumulado do pedido para o grupo B em comparação com o grupo A.
# 

# <font color='gray'>para tanto, uniremos novamente os dados dos grupos A e B em uma tabela, mas agora em colunas apartadas, ou seja, cada coluna se refere a apenas um grupo

# In[29]:


comprasAcumulada.columns=[['data','grupo','compras','clientes','receita']]


# In[31]:


comprasacumuladasjuntas = comprasAcumuladaA.merge(comprasAcumuladaB, left_on='date', right_on='date', how='left', suffixes=['A', 'B'])
comprasacumuladasjuntas.columns


# agora é so plotar o grafico

# In[32]:


plt.figure(figsize=(16,8))
plt.plot(comprasacumuladasjuntas['date'], (comprasacumuladasjuntas['revenueB']/comprasacumuladasjuntas['transactionIdB'])/(comprasacumuladasjuntas['revenueA']/comprasacumuladasjuntas['transactionIdA'])-1)
plt.axhline(y=0, color='black', linestyle='--')
plt.axhline(y=0.25, color='gray', linestyle='--')

plt.figure()


# 
# <font color='blue'>2. conclusões e conjecturas.

# <font color='green'>Em vários pontos, a diferença entre os segmentos apresenta picos. 
# Isso indica a ocorrência de pedidos grandes e valores atípicos! Vamos encontrá-los depois. Destaco o dia 18.

# ### Subseção 2.5: Tarefa 4: Taxa de conversão diária e diferença relativa na conversão cumulativa 
# <a class="" id='subseção-25'></a>
# 
# 

# <font color='blue'>1. Calcular a taxa de conversão de cada grupo como a proporção de pedidos para o número de visitas para cada dia.

# <font color='gray'>repetimos o procedimento de forma semelhante, 
# dividindo a tabela nos grupos A e B, para obter os valores da taxa de conversao acumulada, para cada grupo.

# In[33]:


# calculando a conversão cumulativa
dadosAcumuladosA=dadosAcumulados[dadosAcumulados['group']=='A']
dadosAcumuladosB=dadosAcumulados[dadosAcumulados['group']=='B']


# In[34]:


dadosAcumuladosA.columns


# In[35]:


dadosAcumuladosA.loc[:,'conversao'] = dadosAcumuladosA.loc[:,'orders']/dadosAcumuladosA.loc[:,'visitors']
dadosAcumuladosB.loc[:,'conversao'] = dadosAcumuladosB.loc[:,'orders']/dadosAcumuladosB.loc[:,'visitors']


# In[36]:


dadosAcumuladosA.columns


# <font color='blue'>2. Traçar as taxas de conversão diárias dos dois grupos e descrever a diferença.

# In[37]:


# construindo os gráficos
plt.figure(figsize=(15,8))
plt.plot(dadosAcumuladosA['date'], dadosAcumuladosA['conversao'], label='A')
plt.plot(dadosAcumuladosA['date'], dadosAcumuladosB['conversao'], label='B')
plt.title('Taxa de Conversão Diária')

plt.legend()


# <font color='green'>percebe-se que o Grupo B alcançou visivelmente mais conversão de visitas em compras do que o grupo A

# <font color='blue'>3. Fazer um gráfico da diferença relativa na conversão cumulativa para o grupo B em comparação com o grupo A.

# a conversão relativa segue a formula: 
# conversao_retaliva= (B/A) - 1

# In[38]:


mergedCumulativeConversions = dadosAcumuladosA[['date','conversao']].merge(dadosAcumuladosB[['date','conversao']], left_on='date', right_on='date', how='left', suffixes=['A', 'B'])
plt.figure(figsize=(15,10))
plt.plot(mergedCumulativeConversions['date'], mergedCumulativeConversions['conversaoB']/mergedCumulativeConversions['conversaoA']-1)

plt.axhline(y=0, color='black', linestyle='--')
plt.axhline(y=0.15, color='grey', linestyle='--')


# <font color='blue'>4. Tirar conclusões e criar conjecturas.

# <font color='green'>a conversão do grupo B foi notoriamente maior, entretanto vemos alguns picos, o que pode ser em razãoo de outliers

# ### Subseção 2.6: Tarefa 5: Identificação de anomalias nos dados 
# <a class="" id='subseção-26-tarefa-5-identificação-de-anomalias-nos-dados'></a>
# 
# 

# <font color='blue'>1. Calcular os percentis 95 e 99 para o número de pedidos por usuário.

# In[39]:


ordersByUsers=pedidoslimpo.groupby('visitorId').agg({'transactionId':'nunique'}).reset_index().sort_values(by='transactionId',ascending=False)

ordersByUsers.columns = ['userId', 'orders']

print(np.percentile(ordersByUsers['orders'], [90, 95, 99]))


# <font color='blue'>2. Definir o ponto em que um ponto de dados se torna uma anomalia.</font>

# acima de 2 será considerado anormal

# In[40]:


pedidosPorUsuariosAnormal=3


# <font color='blue'>3. Fazer um gráfico de dispersão dos preços dos pedidos.</font>

# aqui um grafico de caixa e bigode seria bom também

# In[41]:


plt.figure(figsize=(15,8))

x_values = pd.Series(range(0,len(pedidoslimpo)))

plt.scatter(x_values, pedidoslimpo['revenue']) 


# In[42]:


plt.figure(figsize=(15,8))
plt.scatter(pedidoslimpo['date'],pedidoslimpo['revenue'])


# <font color='blue'>4. Calcular os percentis 95 e 99 dos preços dos pedidos.

# In[43]:


print('os percentis 95 e 99 dos preços dos pedidos: ', np.percentile(pedidoslimpo['revenue'], [95, 99])) 


# In[44]:


media = np.mean(pedidoslimpo['revenue'])
desvio_padrao = np.std(pedidoslimpo['revenue'])


limite_superior = media + 3 * desvio_padrao
limite_inferior = media - 3 * desvio_padrao
print(limite_superior)


# <font color='blue'>5. Definir o ponto em que um ponto de dados se torna uma anomalia.</font>

# <font color='green'>pelo critério de 3 vezes o desvio padrão temos 2074, mas pelo criterio dos percentis, é razoavel escolher 800, pois quasse 99% da população estará dentro do padrão.
# 

# In[45]:


precoanormal=800


# ### Subseção 2.7: Tarefa 6: Teste de significância estatística <a class="" id='subseção-27-tarefa-6-teste-de-significância-estatística'></a>
# 

# <font color='green'>Hipotese nula: ambas as amostras (grupo A e grupo B) são estatisticamente iguais
#     
# <font color='red'>Hipotese alternativa: um grupo desempenhou melhor que outro  

# <font color='blue'>1. Encontrar a significância estatística da **diferença na conversão** entre os grupos usando os **dados brutos**.</font>

# In[ ]:


import scipy.stats as stats
ordersByUsersA = pedidoslimpo[pedidoslimpo['group']=='A'].groupby('visitorId', as_index=False).agg({'transactionId' : pd.Series.nunique})
ordersByUsersA.columns = ['userId', 'orders']

ordersByUsersB = pedidoslimpo[pedidoslimpo['group']=='B'].groupby('visitorId', as_index=False).agg({'transactionId' : pd.Series.nunique})
ordersByUsersB.columns = ['userId', 'orders']


# <font color='gray'>aqui a gente considera que o numero excedente de visitas, foi de usuarios que nada compraram, portanto, uma vez que trabalhamos com dados que não tem os ids das visitas(apenas os das compras), temos que adicionar ao dataframe usuarios ficticios que visitaram e nada compraram.
# 

# In[ ]:


sampleA = pd.concat([ordersByUsersA['orders'],pd.Series(0, index=np.arange(visitas[visitas['group']=='A']['visits'].sum() - len(ordersByUsersA['orders'])), name='orders')],axis=0)

sampleB = pd.concat([ordersByUsersB['orders'],pd.Series(0, index=np.arange(visitas[visitas['group']=='B']['visits'].sum() - len(ordersByUsersB['orders'])), name='orders')],axis=0)


# In[57]:


print("{0:.5f}".format(stats.mannwhitneyu(sampleA, sampleB)[1]))

print("{0:.5f}".format(sampleB.mean()/sampleA.mean()-1))


# <font color='green'>A primeira linha do resultado nos dá o valor-p, 0.011, que é bem menor que 0.05. Então, podemos rejeitar a hipótese nula (de que não há diferença estatística significativa na conversão entre os grupos). O grupo B foi 16% (melhor que o A).

# <font color='blue'>2. Encontrar a significância estatística da **diferença no tamanho médio do pedido** entre os grupos usando os **dados brutos**.</font>

# In[47]:


print('{0:.3f}'.format(stats.mannwhitneyu(pedidoslimpo[pedidoslimpo['group']=='A']['revenue'], pedidoslimpo[pedidoslimpo['group']=='B']['revenue'])[1]))
print('{0:.3f}'.format(pedidoslimpo[pedidoslimpo['group']=='B']['revenue'].mean()/pedidoslimpo[pedidoslimpo['group']=='A']['revenue'].mean()-1)) 


# <font color='green'>O valor-p é muito maior do que 0.05, então não há motivo para rejeitar a hipótese nula e concluir que o volume médio de pedidos seria diferente entre os grupos.
# O volume médio de pedidos do grupo B é muito maior do que o do grupo A.

# <font color='blue'>3. Encontrar a significância estatística  da **diferença na conversão** entre os grupos usando os **dados filtrados**.</font>

# In[48]:


pedidoslimpo.columns


# In[49]:


usersWithManyOrders = pd.concat([ordersByUsersA[ordersByUsersA['orders'] > 2]['userId'], ordersByUsersB[ordersByUsersB['orders'] > 2]['userId']], axis = 0)
usersWithExpensiveOrders = pedidoslimpo[pedidoslimpo['revenue'] > 800]['visitorId']
abnormalUsers = pd.concat([usersWithManyOrders, usersWithExpensiveOrders], axis = 0).drop_duplicates().sort_values()
print(abnormalUsers.head(5))
print(abnormalUsers.shape) 


# In[50]:


sampleAFiltered = pd.concat([ordersByUsersA[np.logical_not(ordersByUsersA['userId'].isin(abnormalUsers))]['orders'],pd.Series(0, index=np.arange(visitas[visitas['group']=='A']['visits'].sum() - len(ordersByUsersA['orders'])),name='orders')],axis=0)

sampleBFiltered = pd.concat([ordersByUsersB[np.logical_not(ordersByUsersB['userId'].isin(abnormalUsers))]['orders'],pd.Series(0, index=np.arange(visitas[visitas['group']=='B']['visits'].sum() - len(ordersByUsersB['orders'])),name='orders')],axis=0)


# <font color='gray'>sem filtro:

# <font color='gray'>dado bruto:

# In[51]:


print("p-value:","{0:.5f}".format(stats.mannwhitneyu(sampleA, sampleB)[1]))

print("relação","{0:.5f}".format(sampleB.mean()/sampleA.mean()-1))


# <font color='gray'>dado sem outliers:

# In[52]:


print("p-value:","{0:.5f}".format(stats.mannwhitneyu(sampleAFiltered, sampleBFiltered)[1]))
print("relação","{0:.5f}".format(sampleBFiltered.mean()/sampleAFiltered.mean()-1)) 


# <font color='blue'>4. Encontrar a significância estatística da diferença no **tamanho médio do pedido** entre os grupos usando os **dados filtrados**.</font>

# <font color='gray'>dados bruto:

# In[53]:


print("p-value:",'{0:.3f}'.format(stats.mannwhitneyu(pedidoslimpo[pedidoslimpo['group']=='A']['revenue'], pedidoslimpo[pedidoslimpo['group']=='B']['revenue'])[1]))
print("relação",'{0:.3f}'.format(pedidoslimpo[pedidoslimpo['group']=='B']['revenue'].mean()/pedidoslimpo[pedidoslimpo['group']=='A']['revenue'].mean()-1)) 


# <font color='gray'>dado sem outliers:

# In[54]:


print("p-value:",'{0:.3f}'.format(stats.mannwhitneyu(
    pedidoslimpo[np.logical_and(
        pedidoslimpo['group']=='A',
        np.logical_not(pedidoslimpo['visitorId'].isin(abnormalUsers)))]['revenue'],
    pedidoslimpo[np.logical_and(
        pedidoslimpo['group']=='B',
        np.logical_not(pedidoslimpo['visitorId'].isin(abnormalUsers)))]['revenue'])[1]))

print("relação",'{0:.3f}'.format(
    pedidoslimpo[np.logical_and(pedidoslimpo['group']=='B',np.logical_not(pedidoslimpo['visitorId'].isin(abnormalUsers)))]['revenue'].mean()/
    pedidoslimpo[np.logical_and(
        pedidoslimpo['group']=='A',
        np.logical_not(pedidoslimpo['visitorId'].isin(abnormalUsers)))]['revenue'].mean() - 1)) 


# <font color='gray'>media sem outliers:

# In[62]:


print("media volume de compra grupo B",pedidoslimpo[np.logical_and(
        pedidoslimpo['group']=='B',
        np.logical_not(pedidoslimpo['visitorId'].isin(abnormalUsers)))]['revenue'].mean())
print("media volume de compra grupo A",pedidoslimpo[np.logical_and(
        pedidoslimpo['group']=='A',
        np.logical_not(pedidoslimpo['visitorId'].isin(abnormalUsers)))]['revenue'].mean())


# <font color='blue'>5. Tirar conclusões e criar conjecturas.</font>

# <font color='green'>Conclui-se que os dados filtrados demonstram nitidamente que houve mais conversão em compras com o grupo B. Podemos rejeitar a hipotese nula de que A e B são iguais estatisticamente. Além disso, não há qualquer indicio de que houve variação significativa quanto ao volume médio de cada compra.

# 
# 
# ### Subseção 2.8: Tarefa 7: Tomada de decisão 
# 
# <a class="" id='seção-28'></a>
# 
# 

# <font color='blue'> Decidir com base nos resultados do teste. 
# As decisões possíveis são: 
# 1. Pare o teste, considere um dos grupos o líder. 
# 2. Pare o teste, conclua que não há diferença entre os grupos. 
# 3. Continue o teste.

# - [Sumário](#sumário)
# 
# ## Seção 3: Conclusões Gerais 
# <a class="" id='seção-3-conclusões-gerais'></a>

# <font color='green'> Analisando, conclui-se pela possibilidade de parar o teste e considerar o grupo B mais eficaz em converter visitantes para clientes.
