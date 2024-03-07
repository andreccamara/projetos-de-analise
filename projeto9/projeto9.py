#!/usr/bin/env python
# coding: utf-8

# # Sumário
# <a id='sumario'></a>
# - [sumario](#sumario)
# - [Carregando dados](#carregando-dados)
# - [Análise de dados](#analise-de-dados)
#   - [Investigando as proporcoes dos vários tipos de estabelecimentos](#i1)
#     - [Gráfico](#g1)
#   - [Investigando as proporcoes de estabelecimentos de rede](#iv)
#     - [Gráfico](#grafico2)
#   - [Qual tipo de estabelecimento é típico para redes?](#iv-rede)
#   - [O que caracteriza redes: muitos estabelecimentos com um pequeno número de assentos? poucos estabelecimentos com muitos assentos?](#redes)
#     - [Número médio de assentos para cada tipo de restaurante](#assentos)
#     - [Em média, qual tipo de restaurante tem o maior número de assentos?](#maior)
#       - [Gráficos](#graficos3)
#   - [Separando os dados dos nomes das ruas da coluna address em uma coluna separada](#ruas)
#     - [Gráfico das dez ruas com o maior número de restaurantes](#top10)
#     - [Encontrando o número de ruas que têm apenas um restaurante](#so1)
#     - [Análise das ruas com muitos restaurantes, à luz da distribuição do número de assentos](#distribuicao)
#     - [Conclusões sobre tendências](#conclusao)     
# - [apresentando](#apresentacao)

# [sumario](#sumario)
# # Carregando dados <a class="" id="carregando-dados"></a>

# In[1]:


#importando bibliotecas
import pandas as pd
import numpy as np
import math as mth
import scipy.stats as stats
from scipy import stats as st
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median
import plotly.express as px
from plotly import graph_objects as go


# In[2]:


plt.style.available


# In[3]:


caminho='rest_data_us.csv'
try:
    restaurantes=pd.read_csv('/datasets/rest_data_us.csv')
except:
    restaurantes=pd.read_csv(caminho)
restaurantes


# In[4]:


restaurantes.info()


# <font color='green'>encontramos alguns valores ausentes (3) na coluna booliana, entende-se que a ausencia significa False.

# In[5]:


restaurantes.loc[restaurantes['chain'].isnull(), 'chain'] = False
restaurantes.loc[restaurantes['chain'].isnull()]


# In[6]:


restaurantes['chain'] = restaurantes['chain'].astype(bool)


# In[7]:


restaurantes=restaurantes.drop_duplicates()


# In[8]:


restaurantes.columns = ['id', 'nome', 'endereco', 'rede', 'tipo', 'assento']


# [sumario](#sumario)
# 
# # Analise de dados <a class="" id="analise-de-dados"></a>

# agora que os dados estão limpos, vamos analizá-los.

# [sumario](#sumario)
# ## Investigando as proporções dos vários tipos de estabelecimentos.  
# <a  id='i1'> </a>

# In[9]:


tipoderestaurante=restaurantes.groupby('tipo').agg({'id':'count'}).reset_index().sort_values(by='id', ascending=False)
tipoderestaurante


# 
# a maioria são restaurantes, depois fast foods

# [sumario](#sumario)
# ### grafico. 
# <a id='g1'> </a>

# In[45]:


with plt.style.context('seaborn-deep'):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='tipo', y='id', data=tipoderestaurante)
    plt.title('quantidade de estabelecimentos')


# In[11]:


fig=go.Figure(data=[go.Pie(labels=tipoderestaurante['tipo'], values=tipoderestaurante['id'])])

fig.show()


# In[12]:


colors = sns.color_palette('dark')
fig, conf = plt.subplots()
conf.set_title('tipos de estabelecimentos')
plt.pie(tipoderestaurante['id'], labels=tipoderestaurante['tipo'], colors=colors)

fig.set_figheight(6) # alterando a altura
fig.set_figwidth(8) # alterando a largura


# [sumario](#sumario)
# ## Investigando as proporcoes, se pertencem ou não a redes. 
# <a id= 'iv'> </a>

# In[13]:


chain=restaurantes.groupby('rede').agg({'id':'count'}).reset_index()


# In[14]:


restaurantes


# In[15]:


chain


# In[16]:


prop=chain.loc[0]['id']/chain.loc[1]['id']
print("Tem {:.2f} vezes mais restaurantes não ligados a redes do que ligados a redes".format(prop))


# [sumario](#sumario)
# ### gráfico. 
# <a id='grafico2'> </a>

# In[17]:


chain


# In[18]:


sns.barplot(x= 'rede',
y= 'id',
data=chain)


# In[19]:


sns.countplot(data=restaurantes, x="rede")


# In[20]:


restaurantes.columns


# In[21]:


sns.countplot(data=restaurantes, x="rede", hue='tipo')
plt.title("quantidade por tipos")


# [sumario](#sumario)
# ## Qual tipo de estabelecimento é típico para redes? 
# <a id='iv-rede'> </a>

# In[22]:


naorede=restaurantes[restaurantes['rede']==False]
rede=restaurantes[restaurantes['rede']==True]
naoredetipoobj=naorede.groupby('tipo').agg({'id':'count'}).reset_index()
redetipoobj=rede.groupby('tipo').agg({'id':'count'}).reset_index()


# vendo a porcentagem de estabelecimentos que pertem a redes, dividido por tipo.

# In[23]:


tipomedia=restaurantes.groupby('tipo').mean().reset_index()
tipomedia


# In[68]:


tipomediae=tipomedia.drop('id', axis=1)
tipomediae[[ 'rede', 'assento']] = tipomedia[['rede', 'assento']].round(2)
tipomediae


# In[70]:


tipomediae=tipomediae.rename(columns={'tipo':'tipo','rede':'porcentagem','assento':'assentos'})
# Exibindo o DataFrame
print(tipomediae)


# In[46]:


tipomedia.plot.bar(x='tipo', y='rede', title='porcentagem ligada a franquias/redes')


# In[25]:


fig1 = go.Figure(data=go.Pie(values=naoredetipoobj['id'], labels=naoredetipoobj['tipo']))
fig1.update_layout(title='Gráfico de Pizza - Não Redes')

fig1.show()
fig2=go.Figure(data=go.Pie(labels=redetipoobj['tipo'], values=redetipoobj['id']))
fig2.update_layout(title='Gráfico de Pizza - Redes')

fig2.show()


# <font color='green'>apesar de numericamente termos mais restaurantes ligado a redes, proporcionalmente são os fastfoods, as pizzarias, os cafés e principalmente os bakery os estabelecimentos tipicamente de redes. Restaurantes e bares não são proporcionalemnte tão ligados a redes

# [sumario](#sumario)
# ## O que caracteriza redes: muitos estabelecimentos com um pequeno número de assentos? poucos estabelecimentos com muitos assentos?
# <a id='redes'> </a>

# In[26]:


naorede


# In[27]:


naorede['assento'].describe()


# In[28]:


rede['assento'].describe()


# comparativamente temos menos assentos nas redes, alem disso a moda é bem menor que a média, o que indica que tem alguns valores altos puxando a média, que já é baixa.

# [sumario](#sumario)
# ### Número médio de assentos para cada tipo de restaurante. 
# <a id='assentos'> </a>

# In[29]:


tipomedia=restaurantes.groupby('tipo').mean().reset_index()


# In[30]:


resp41=tipomedia.apply(lambda x: print("{:<12} {:.2f}".format(x['tipo'], x['assento'])), axis=1)
resp41


# [sumario](#sumario)
# ### Em média, qual tipo de restaurante tem o maior número de assentos? 
# <a id='maior'> </a>

# [sumario](#sumario)
# #### gráficos.
# <a id='graficos3'> </a>

# In[73]:


ax = sns.barplot(x='tipo', y='assento', data=tipomedia)

# Adicionando título ao gráfico
ax.set_title('quantidade media de assentos')

# Exibindo o gráfico
plt.show()


# In[32]:


assentos=go.Figure(data=go.Pie(labels=tipomedia['tipo'], values=tipomedia['assento']))
assentos


# <font color = 'green'> restaurantes, bares e fastfoods têm mais assentos, enquanto padarias e cafés têm menos.  
#     Por um lado é compreensivo, pois padarias e cafés, vendem muito para viagem, enquanto restaurantes e bares não.    
# Além disso restaurantes e bares tendem a acomodar clientes por muito mais tempo. O que surpreende é o fato de pizzarias terem menos de 30 assentos em média. </font>

# [sumario](#sumario)
# ## semparando os dados dos nomes das ruas da coluna address em uma coluna separada.
# <a id='ruas'> </a>

# In[ ]:


import re

lambda passa a função replace() nos elementos do obj series restaurantes['endereco']  
a função pega o dado e procura a parte numerica simbolizada por \d+ e troca por '', ou seja vazio.  
o r' serve apenas para reconhecer todos os caracteres especiais seguintes literalmente;
ocaractere ^ ancora no inicio da linha;  
O caractere | simboliza alternancia;
Já o /b significa espaço em branco;
os simbolos .* simbolizam tudo o que vier após o caractere anterior (# ou STE no exemplo).
Por fim,o $ simboliza o fim da linha
# In[34]:


restaurantes['ruas'] = restaurantes['endereco'].apply(lambda dado: re.sub(r'^\d+|#.*|\bSTE\b.*|\bST\b.*', '', dado))



# In[35]:


restaurantes


# In[36]:


restaurantes['ruas'].unique()


# In[74]:


restaurantes['ruas'].nunique()


# [sumario](#sumario)
# ### gráfico das dez ruas com o maior número de restaurantes.
# <a id='top10'> </a>

# In[134]:


ruasr=restaurantes.groupby('ruas').agg({'id':'count'}).reset_index().sort_values(by='id', ascending=False)
top10=ruasr.head(10)
print(top10)


# In[136]:


ruasr


# In[137]:


ruasr.columns=['ruas','total']


# In[138]:


ruasr['total'].sum()


# In[140]:


ruasr2=ruasr
ruasr2['percentual']=ruasr['total']*100/ruasr['total'].sum()
ruasr2['percentual'] = ruasr2['percentual'].round(2)
x=ruasr2.head(10)
x


# In[141]:


x['percentual'].sum()


# In[83]:


print(top10['ruas'].reset_index(drop=True))


# In[84]:


top10.plot(x='ruas',y='id',kind='bar')


# In[85]:


contagemruas=restaurantes.groupby('ruas').agg({'id':'count'})


# In[86]:


contagemruas.mean()


# In[87]:


contagemruas.describe()


# In[88]:


contagemruas.tail()


# In[89]:


contagemruas.sort_values(by='id')


# [sumario](#sumario)
# ### encontrando o número de ruas que têm apenas um restaurante.
# <a id='so1'> </a>

# In[90]:


dfrua=restaurantes.groupby('ruas').agg({'id':'count'}).reset_index()
dfrua.columns=['rua','restaurantes']
print("quantidade de ruas com apenas um restaurante:", dfrua[dfrua['restaurantes']==1]['restaurantes'].count())


# <font color = 'green'>temos algumas ruas com mais de 100 estabelecimetnos, as 2 maiores rua têm quase 300 estabelecimentos. As outras 8 têm mais de 100. Creio que sejam avenidas comerciais, provavelmente no centro comercial da cidade. A média de estabelecimentos por rua é 7,3. O que é muito pequeno, a maioria(620), inclusive, só tem um estabelecimento. 

# [sumario](#sumario)
# ### Analise das ruas com muitos restaurantes, à luz da distribuição do número de assentos.
# <a id='distribuicao'> </a>

# In[91]:


#vamos comparar o banco de dados com apenass os dados das 10 ruas com mais estabelecimentos


# In[92]:


top10.columns


# In[93]:


restaurantes.columns


# In[94]:


top10


# In[95]:


top10ruas=restaurantes[restaurantes['ruas'].isin(top10['ruas'])].reset_index().drop('index',axis=1)
top10ruas


# In[96]:


top10ruas['ruas'].nunique()


# In[97]:


gruporuaassento=top10ruas.groupby('ruas').agg({'assento':'mean'}).reset_index()
gruporuaassento


# In[98]:


graficoruaassento=go.Figure(data=[go.Pie(labels=gruporuaassento['ruas'], values=gruporuaassento['assento'])])

graficoruaassento.show()


# In[99]:


gruportipoassento=top10ruas.groupby('tipo').agg({'assento':'mean'}).reset_index()
gruportipoassento


# In[100]:


assentotipo=restaurantes.groupby('tipo').agg({'assento':'mean'}).reset_index()
assentotipo


# In[101]:


sns.countplot(data=top10ruas, x="tipo")
plt.title("quantidade por tipos")


# In[102]:


sns.countplot(data=restaurantes, x="tipo")
plt.title("quantidade por tipos")


# In[103]:


toptipomedia=top10ruas.groupby('tipo').mean().reset_index()
toptipomedia


# In[104]:


tipomedia=restaurantes.groupby('tipo').mean().reset_index()
tipomedia


# In[105]:


y = restaurantes['assento']
plt.figure(figsize=(15, 8))
plt.scatter(restaurantes.index, y, color='blue', alpha=0.7)
plt.ylabel('assentos')
plt.show()


# In[106]:


'''sns.stripplot(x= 'endereco' ,y= 'assento', data=top10ruas)'''
y = top10ruas['assento']
plt.figure(figsize=(15, 8))
plt.scatter(top10ruas.index, y, color='blue', alpha=0.7)
plt.ylabel('assentos')
plt.show()



# In[107]:


plt.figure(figsize=(15, 8))
plt.hist(top10ruas['assento'], bins=20)
plt.ylabel('assentos')
plt.show()


# In[108]:


plt.figure(figsize=(15, 8))
plt.hist(restaurantes['assento'], bins=20)
plt.ylabel('assentos')
plt.show()


# In[109]:


restaurantes['assento'].describe()


# In[110]:


print(np.percentile(top10ruas['assento'], 95),
top10ruas['assento'].quantile(0.99))


# In[111]:


print(np.percentile(restaurantes['assento'], 95),
restaurantes['assento'].quantile(0.99))


# In[112]:


top10ruasfil=top10ruas[top10ruas['assento']<=145]
restaurantesfil=restaurantes[restaurantes['assento']<=145]


# In[113]:


fig, graf = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plotar violinplot para top10ruas
sns.violinplot(y='assento', data=top10ruas, ax=graf[0])
graf[0].set_title('Top 10 Ruas')
graf[0].set_ylabel('Número de Assentos')
graf[0].set_xlabel('')

# Plotar violinplot para restaurantes
sns.violinplot(y='assento', data=restaurantes, ax=graf[1])
graf[1].set_title('Todos os Restaurantes')
graf[1].set_ylabel('Número de Assentos')
graf[1].set_xlabel('')

# Ajustar layout
plt.tight_layout()

# Mostrar os subplots
plt.show()


# In[114]:


fig, pontos = plt.subplots(nrows=2, ncols=1, figsize=(20, 6))
y = restaurantesfil['assento']
pontos[0].scatter(restaurantesfil.index, y, color='blue', alpha=0.7,)
pontos[0].set_title('Todos os Restaurantes')


y2 = top10ruasfil['assento']
pontos[1].scatter(top10ruasfil.index, y2, color='blue', alpha=0.7)
pontos[1].set_title('top 10 ruas')
plt.show()


# In[115]:


fig, pontos = plt.subplots(nrows=2, ncols=1, figsize=(20, 6))
y = restaurantesfil['assento']
pontos[0].hist( y)
pontos[0].set_title('Todos os Restaurantes')


y2 = top10ruasfil['assento']
pontos[1].hist( y2)
pontos[1].set_title('top 10 ruas')
plt.show()


# In[116]:


top10ruasfil=top10ruas[top10ruas['assento']<=60]
restaurantesfil=restaurantes[restaurantes['assento']<=60]


# In[117]:


fig, pontos = plt.subplots(nrows=2, ncols=1, figsize=(20, 6))
y = restaurantesfil['assento']
pontos[0].hist( y)
pontos[0].set_title('Todos os Restaurantes')


y2 = top10ruasfil['assento']
pontos[1].hist( y2)
pontos[1].set_title('top 10 ruas')
plt.show()


# [sumario](#sumario)
# ### conclusões sobre tendencias
# <a id='conclusao'> </a>

# <font color = 'blue'>nove das 10 ruas mais movimentadas possuem em media mais de 40 assentos por estabelecimento, o que me faz concluir que as ruas mais movimentadas possuem estabelecimentos maiores. Entretanto a tendencia de assentos geral e das ruas mais movimentadas é a mesma.

# [sumario](#sumario)
# # Apresentacao 
# <a id='apresentacao'> </a>

# <div class="alert alert-block alert-info">
#     <b>
#     Link da apresentação: 
#     </b> 
#         
# https://drive.google.com/file/d/1nr1m781EEO0GY1AWbel3U2Vi6nJ_vXvp/view?usp=drive_link
#     
#   
# 
# 
