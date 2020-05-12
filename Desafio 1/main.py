#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[6]:


import pandas as pd
import numpy as np


# In[9]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[12]:


black_friday.head()


# In[15]:


black_friday.index


# In[18]:


black_friday.columns


# In[21]:


black_friday.info()


# In[24]:


black_friday.nunique()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[27]:


def q1():
    # Retorne aqui o resultado da questão 1.
    pass
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[30]:


def q2():
    # Retorne aqui o resultado da questão 2.
    pass 
    return(black_friday.query("Age == '26-35' & Gender == 'F'")['User_ID'].shape[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[33]:


def q3():
    # Retorne aqui o resultado da questão 3.
    pass                        
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[36]:


def q4():
    # Retorne aqui o resultado da questão 4.
    pass
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[39]:


def q5():
    # Retorne aqui o resultado da questão 5.
    pass
    no_null = black_friday.shape[0] - black_friday.dropna().shape[0]
    return no_null/black_friday.shape[0]


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[42]:


def q6():
    # Retorne aqui o resultado da questão 6.
    pass
    return int(black_friday.isnull().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[45]:


def q7():
    # Retorne aqui o resultado da questão 7.
    pass
    black_friday_no_null = black_friday.dropna()
    return float(black_friday_no_null['Product_Category_3'].mode())


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[48]:


def q8():
    # Retorne aqui o resultado da questão 8.
    pass
    black_friday_max = black_friday['Purchase'].max()
    black_friday_min = black_friday['Purchase'].min()
    result = (black_friday['Purchase'] - black_friday_min)/(black_friday_max - black_friday_min)
    return float(result.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[51]:


def q9():
    # Retorne aqui o resultado da questão 9.
    pass
    purchase = black_friday['Purchase']
    padronization = (purchase - purchase.mean()) / (purchase.std())
    return int(((padronization >= -1) & (padronization <= 1)).sum())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[52]:


def q10():
    # Retorne aqui o resultado da questão 10.
    pass
    compare = black_friday['Product_Category_2'].isnull() == black_friday['Product_Category_3'].isnull()
    return (True in compare)

