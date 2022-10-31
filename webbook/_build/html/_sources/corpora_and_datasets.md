# Corpora and Datasets

Corpus-based research builds on top of collections of data 

An introduction to interacting with the Carnatic and Hindustani portion of the Dunya corpora [2] and the derivative dataset, Saraga, a large and open dataset, compiled and organized alongside experts and practitioners of the traditions [3]. We also present the tools that can be used to access and interact with the data, e.g. PyCompMusic [4], mirdata [5] or MusicBrainz [6].

## Dunya corpora
Dunya comprises the music corpora and related software tools that have been developed as part of the CompMusic project. These corpora have been created with the aim of studying particular music traditions and they include audio recordings plus complementary musically-relevant metadata, expert annotations, and automatically-extracted features. 

The metadata is provided by [MusicBrainz](https://musicbrainz.org/). You can use MusicBrainz to browse the recordings included in the Dunya corpora and the respective metadata. In fact, all recordings in Dunya are tagged with a MusicBrainzID (stylized as ``mbid``), which also serves as a unique identifier for each entry in the Dunya database.

In Dunya, each corpus has specific characteristics and the developed software tools allow to process the available information in order to study and explore the characteristics of each musical repertoire. Let us now review the tools to access, browse, and parse the data in the Dunya corpora:


### Dunya website
You can browse through the Dunya corpora using [the Dunya website](https://dunya.compmusic.upf.edu/). 

```{figure} ./images/dunya_1.png
---
alt: Dunya traditions
name: dunya_traditions
---
Musical traditions represented in the Dunya corpora
```

Although focusing on Carnatic and Hindustani music in this tutorial, note that Dunya opens the door for computational research of other traditions too! The Dunya website includes also an interactive interface to listen to some examples of the data in the corpora and visualize the available annotations and features.


### Dunya Python API
The data in Dunya can be programatically browsed, parsed and downloaded using the Dunya Python API in [pycompmusic](https://dunya.compmusic.upf.edu/docs/search.html). We have ported pycompmusic into compIAM, so the corpora can be accessed through compIAM as well. Through this software, you can parse statistics in the databaset, while the data in Dunya can be filtered by tradition, artist, raaga, taala. 

```{note}
To access the data in Dunya, you need a personal access token. You get the said token by registering to Dunya using the website.
```

You can easily initialize a Corpora instance of compIAM as:
```python
from compiam import load_corpora
carnatic_corpora = load_corpora("carnatic", cc=True, token="your-token-goes-here")
```

```{note}
Carnatic and Hindustani corpora are both divided in two parts, one part licensed under Creative Commons 4.0 which can be openly shared for research purposes, while the other part is restricted and is only shared under an explicit research-related request. You can request access to the non-CC part of the corpora through the Dunya website. If granted, your access token will allow you to access these data. Set the cc parameter to False in ``compiam.load_corpora()`` to load these collection.
```

Our corpora class include methods to get an overview of the available data in the database. Let us get you some examples below:

* ``get_collection()``: prints you out all available recordings in the collection.
* ``get_recording(mbid=<specific-musicbrainz-id>)``: given a MusicBrainz ID, prints out the available data for the associated recording.
* ``get_recording(mbid=<specific-musicbrainz-id>)``: given a MusicBrainz ID, prints out the available data for the associated recording.


## Datasets
### `mirdata`
[mirdata](https://mirdata.readthedocs.io/en/stable/) is an open-source and pip-installable Python library that provides tools for working with common Music Information Retrieval (MIR) datasets. Given the crucial importance and relevance of such a software for data and corpus-driven research, we have done a great effort integrating several IAM-centered datasets in mirdata. To date, the following datasets can be found in the latest mirdata release:

* Carnatic collection of Saraga [x]
* Hindustani collection of Saraga [x]
* Carnatic Varnam Dataset [x]
* Carnatic Music Rhythm [x]
* Hindustani Music Rhythm [x]
* Indian Art Music Raga Dataset [x]
* Mridangam Stroke Dataset [x]
* Four-Way Tabla Dataset (ISMIR 2021) [x]

compIAM provides access to these datasets through the mirdata loaders. Therefore, by using an alias of mirdata method ``mirdata.initialize()`` as ``compiam.initialize()`` you can also access the datasets
integrated to mirdata!

