(corpora)=
# Accessing the Dunya Corpora
In a computer science context, a corpus is a large collection of data and annotations. Corpus-based research should build on top of collections of data that have been designed with a **purpose**, have **good coverage**, are **complete**, the data have **good quality**, and finally that ensures **reusability** {cite}`serra_2014`. The research built on top of these collections of data ensures *real-world results*. The corpora in Dunya, built within the context of the CompMusic project, have been designed taking these requirements into account.

## What do the corpora include?
The corpora in Dunya include audio recordings plus complementary musically-relevant metadata, expert annotations, and automatically-extracted features.

The metadata is provided by [`MusicBrainz`](https://musicbrainz.org/). You can use `MusicBrainz` to browse the recordings included in the Dunya corpora and the respective metadata. In fact, all recordings in Dunya are tagged with a MusicBrainzID (stylized as ``mbid``), which also serves as a unique identifier for each entry in the Dunya database.

| **Content types**       | **Brief description**                                                                                            |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| **Audio**               | Music mixtures, in some cases accompanied by multi-track audio for particular instruments                        |
| **Metadata**            | Musically-relevant tags <br> **e.g.** raga, tala, artists, concert, album, instruments                           |
| **Expert annotations**  | Expert and time-aligned annotations for relevant musical concepts <br> **e.g.** sama, melodic phrases, sections  |
| **Computed features**   | Features computed using baseline methods <br> **e.g.** pitch tracks, tonic, akshara pulses                      |

In Dunya, each corpus has specific characteristics and the developed software tools allow to process the available information in order to study and explore the characteristics of each musical repertoire. 

Let us now review the tools to access, browse, and parse the data in the Dunya corpora:


## Dunya website
You can browse through the Dunya corpora using [the Dunya website](https://dunya.compmusic.upf.edu/). The Dunya website includes also an interactive interface to listen to some examples of the data in the corpora and visualize the available annotations and features {cite}`dunya`.

```{figure} ../images/dunya_1.png
---
alt: Dunya traditions
name: dunya_traditions
---
Musical traditions represented in the Dunya corpora
```

Although focusing on Carnatic and Hindustani music in this tutorial, note that Dunya opens the door for computational research of other traditions too! 


## Dunya Python API
The data in Dunya can be programatically browsed, parsed and downloaded using the Dunya Python API in [`pycompmusic`](https://dunya.compmusic.upf.edu/docs/search.html). We have ported `pycompmusic` into `compiam`, so the corpora can be accessed through `compiam` as well. Through this software, you can parse statistics in the databaset, while the data in Dunya can be filtered by tradition, artist, raaga, taala. 

```{note}
To access the data in Dunya, you need a personal access token. You get the said token by registering to Dunya through the website.
```

You can easily initialize a Corpora instance of `compiam` as:
```python
from compiam import load_corpora
carnatic_corpora = load_corpora("carnatic", cc=True, token="your-token-goes-here")
```

```{note}
Carnatic and Hindustani corpora are both divided in two parts, one part licensed under Creative Commons 4.0 which can be openly shared for research purposes, while the other part is restricted and is only shared under an explicit research-related request. You can request access to the non-CC part of the corpora through the Dunya website. If granted, your access token will allow you to access these data. Set the cc parameter to False in ``compiam.load_corpora()`` to load these collection.
```

### Browsing the corpora using the API
Our corpora class include methods to get an overview of the available data in the database. Let us get you some examples below:

* ``get_collection()``: prints you out all available recordings in the collection.
* ``get_recording(<recording-musicbrainz-id>)``: prints out the available data for the recording associated with the input mbid.
* ``get_artist(<artists-musicbrainz-id>)``: prints out the available information for the artist associated with the input mbid.
* ``list_concerts()``: list all available concerts in the selected database.
* ``list_available_types(<artists-musicbrainz-id>)``:  prints you out the available types of file available for a particular recording.

See the entire list of methods in the [`compiam` Corpora class documentation](TODO: link).

### Getting the data
The Dunya Python API also provides methods to get the data. You may use these set of functionalities to parse and/or download into your machine a particular annotation, metadata file, or audio track.

* ``get_annotation(<recording-musicbrainz-id>, <annotation-type>)``: download annotation from database given a recording id and the annotation type.
* ``save_annotation(<recording-musicbrainz-id>, <annotation-type>, <path/to/save>)``: an extension of ``get_annotation()`` but writing the annotation to a file.
* ``download_mp3(<recording-musicbrainz-id>, <path/to/save>)``: download and save the audio for a recording.

```{tip}
Loop through a list of ``mbid`` and run the downloading functions to get the data for a specific collection of recordings.
```

