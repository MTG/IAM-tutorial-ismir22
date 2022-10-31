#!/usr/bin/env python
# coding: utf-8

# (datasets)=
# # Datasets
# 
# Datasets are key for the data-driven computational research of a music tradition. Thoroughly designed collections of data that represent the most relevant aspects of a musical repertoire may open the door for solutions of several problems. For that reason, huge efforts have been made within the scope of this tutorial and ``compiam`` to (1) boost the visibility and access to Carnatic and Hindustani music datasets, and (2) provide standardized tools to get and use the said datasets.
# 
# ## `mirdata`
# [mirdata](https://mirdata.readthedocs.io/en/stable/) is an open-source and pip-installable Python library that provides tools for working with common Music Information Retrieval (MIR) datasets. Given the crucial importance and relevance of such a software for data and corpus-driven research, we have done a great efforts to integrate several IAM-centered datasets into mirdata. To date, the following datasets can be found in the latest mirdata release:
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
# `compIAM` provides access to these datasets through the mirdata loaders. 
# 
# ```{note}
# You can use an alias of the mirdata method ``mirdata.initialize()`` as ``compiam.load_dataset()`` to access the mirdata loaders for Indian Art Music datasets from our library!
# ```

# In[1]:


get_ipython().run_cell_magic('capture', '', '# %pip install compiam')


# In[2]:


import compiam
saraga_carnatic = compiam.load_dataset("saraga_carnatic")

## Let's get a random track from the dataset!
saraga_carnatic.choice_track()


# ```{note}
# Run ``compiam.list_datasets()`` to list the available datasets to use.
# ```
# 
# Accessing the datasets through `mirdata` brings numerous advantages and provides a more standardized and easy integration of the said datasets into our pipelines. See:

# In[3]:


import numpy as np

## Loading all tracks from the dataset
carnatic_tracks = saraga_carnatic.load_tracks()

## Get available ragas
available_raagas = np.unique([carnatic_tracks[x].metadata["raaga"] for x in saraga_carnatic.track_ids])
available_raagas


# Grouping recordings per raaga is a common organization strategy for the melodic analysis of Carnatic and Hindustani Music. This is very easy!

# In[ ]:


raaga_dict = {x: [] for x in available_raagas}
for idx in saraga_carnatic.track_ids:
    if carnatic_tracks[idx].metadata["raaga"] is not None:
        raaga_dict[carnatic_tracks[idx].metadata["raaga"]].append(idx)

print("Displaying available tracks for raaga {}: {}"     .format(available_raagas[0], raaga_dict[available_raagas[0]]))


# Cool! However... how about the actual audio and annotations? Let us show how easy is to load the data for a track in the dataset:

# In[ ]:


from IPython.display import Audio

## Selecting a track for a particular raaga
example_track = raaga_dict[available_raagas[0]][0]

## Loading audio directly from track
audio, sr = example_track.audio

## Loading audio from track methods
audio_path = example_track.audio_path  # Audio path of recording
audio_2, sr_2 = example_track.load_audio(audio_path)  # Loading audio

assert audio == audio
assert sr == sr_2

Audio(audio, rate=sr)


# 

# In[ ]:




