#!/usr/bin/env python
# coding: utf-8

# (datasets)=
# # Datasets
# 
# Intro here
# 
# ## `mirdata`
# [mirdata](https://mirdata.readthedocs.io/en/stable/) is an open-source and pip-installable Python library that provides tools for working with common Music Information Retrieval (MIR) datasets. Given the crucial importance and relevance of such a software for data and corpus-driven research, we have done a great effort integrating several IAM-centered datasets in mirdata. To date, the following datasets can be found in the latest mirdata release:
# 
# * Carnatic collection of Saraga [x]
# * Hindustani collection of Saraga [x]
# * Carnatic Varnam Dataset [x]
# * Carnatic Music Rhythm [x]
# * Hindustani Music Rhythm [x]
# * Indian Art Music Raga Dataset [x]
# * Mridangam Stroke Dataset [x]
# * Four-Way Tabla Dataset (ISMIR 2021) [x]
# 
# compIAM provides access to these datasets through the mirdata loaders. Therefore, by using an alias of mirdata method ``mirdata.initialize()`` as ``compiam.initialize()`` you can also access the datasets integrated to mirdata!

# In[1]:


get_ipython().run_cell_magic('capture', '', '%pip install mirdata')


# In[2]:


import mirdata
saraga_carnatic = mirdata.initialize("saraga_carnatic")
saraga_carnatic

