Accessing the Dunya Corpora
===========================

Corpus-based research builds on top of collections of data 

## What do the corpora include?
Dunya comprises the music corpora and related software tools that have been developed as part of the CompMusic project. These corpora have been created with the aim of studying particular music traditions and they include audio recordings plus complementary musically-relevant metadata, expert annotations, and automatically-extracted features. 

The metadata is provided by [MusicBrainz](https://musicbrainz.org/). You can use MusicBrainz to browse the recordings included in the Dunya corpora and the respective metadata. In fact, all recordings in Dunya are tagged with a MusicBrainzID (stylized as ``mbid``), which also serves as a unique identifier for each entry in the Dunya database.

In Dunya, each corpus has specific characteristics and the developed software tools allow to process the available information in order to study and explore the characteristics of each musical repertoire. Let us now review the tools to access, browse, and parse the data in the Dunya corpora:


## Dunya website
You can browse through the Dunya corpora using [the Dunya website](https://dunya.compmusic.upf.edu/). The Dunya website includes also an interactive interface to listen to some examples of the data in the corpora and visualize the available annotations and features.

```{figure} ../images/dunya_1.png
---
alt: Dunya traditions
name: dunya_traditions
---
Musical traditions represented in the Dunya corpora
```

Although focusing on Carnatic and Hindustani music in this tutorial, note that Dunya opens the door for computational research of other traditions too! 


## Dunya Python API
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
* ``get_recording(mbid=<recording-musicbrainz-id>)``: prints out the available data for the recording associated with the input mbid.
* ``get_artist(mbid=<artists-musicbrainz-id>)``: prints out the available information for the artist associated with the input mbid.
* ``list_concerts()``: list all available concerts in the selected database.
* ``list_available_types(mbid=<artists-musicbrainz-id>)``:  prints you out the available types of file available for a particular recording.

Use these functions (check the entire list out in LINK TO DOCUMENTATION) to browse and explore the corpora. The next step is to get the data!

* ``get_annotation(<recording-musicbrainz-id>, <annotation-type>)``: download annotation from database given a recording id and the annotation type.
* ``save_annotation(<recording-musicbrainz-id>, <annotation-type>, <path/to/save>)``: an extension of ``get_annotation()`` but writiing the annotation to a file.
* ``download_mp3(<recording-musicbrainz-id>, <path/to/save>)``: download and save the audio for a recording.
