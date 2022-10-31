#!/usr/bin/env python
# coding: utf-8

# (compiam-melody)=
# # Melodic analysis tools
# 
# In this section we provide an overview of ``compiam.melody``, the module of our library that includes tools to study several relevant melodic aspects of Indian Art Music.
# 
# Let us first start by installing and importing the latest version of ``compiam``.

# In[1]:


get_ipython().run_cell_magic('capture', '', '%pip install compiam\n\nimport compiam')


# As seen in the previous section, predominant and vocal pitch is a very relevant feature to tackle the melodic analysis of Carnatic and Hindustani Music. Let's extract the pitch from an audio sample.

# In[ ]:


from compiam.melody import Melodia
melodia = Melodia()  # initializing a melodia instance
pitch_track = melodia.extract("/path/to/audio")


# Melodia has been found to decently work on Indian Art Music samples (cite MIREX?). However, recent DL-based models have claimed the state-of-the-art for the task of pitch extraction. Maybe we can use a Carnatic-trained version of one of these models to extract the pitch?

# In[ ]:


from compiam.melody import FTANetCarnatic
ftanet_carnatic = FTANetCarnatic()  # initializing a melodia instance
pitch_track = ftanet_carnatic.extract("/path/to/audio")

