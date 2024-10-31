(open-challenges)=
# Open challenges

In this page we review some of the open challenges that remain unsolved or unaddressed in the field of computational musicology for Carnatic and Hindustani Music. 

Please note that this is not an exhaustive list, we only intend to provide, few research ideas and open challenges that may be tackled on top of the work that has been done throughout the past years. 

## Music source separation for Indian Art Music

As already discussed in this tutorial, the problem of source separation in Carnatic and Hindustani Music remains unsolved. While currently available pre-trained models (e.g. Spleeter, Demucs) do not properly generalize to these repertoires, current bespoke solutions for Indian Art Music do not reach the performance level that is achieved for Western modern and mainstream recordings.

The shortage of completely isolated recordings hinders to proper training and testing of DL-based solutions for Carnatic and Hindustani separation. Since these repertoire are normally performed in live performances, it is difficult to gather individual stems that present the ecologically-valid correlation and musical connexion, making the task more complicated.


## Melodic motif discovery

Automatically spotting and understanding melodic motifs and phrases in Carnatic and Hindustani music is key to extract musically relevant information from the recordings. This has been a widely explored problem, with many approaches aiming at discovery characteristic phrases, and also relating those with additional features of the Indian Art Music performances (e.g. video, gestures, and more).

A potential problem in this task is the variability in performance of characteristic/repeated patterns in IAM. Characteristic phrases, when repeated, are often elaborated on, which involves the insertion of additional svaras and gamakas. So the same basic or underlying phrase may appear many times in a composition with different elaborations. The commonly occurs in the style because the main compositional format, the kriti, has a theme and variation structure. Furthermore different IAM musicians’ annotations of the same phrase may vary subtly in places, with different degrees of symbolic detail being possible. This leaves motif detection through time series pitch data as one of the most viable and popular approaches to finding meaningful melodic units in the style {cite}`nuttall_patterns_2022b`.

## Svara-level transcription

Symbolic transcription from audio is an important analytical tool, particularly valuable for the analysis of large audio recording datasets that have never previously been annotated. For IAM, however, such transcription is challenging. In this highly ornamented style, any given svara can be performed in multiple different ways, some of which do not rest on their theoretical pitch positions due to oscillatory ornamentation.

A problem in achieving this task arises due to variation in svara performance, The highly ornamented and oscillatory qualities of the style means that the same svara may be performed in several different ways. However, according to the grammar of the Carnatic style, there are a limited number of ways that a svara may be realized in a given raga (melodic framework), and these ways depend to some extent on immediate melodic context and svara duration.

## Data

Although huge advances have been done towards addressing these tasks, the shortage of expertly annotated/curated data, makes them complicated to tackle and evaluate. We are also concerned with compiling relevant IAM data and in providing tools to easily download and interact with it. Of particular interest is the collection of expert svara and phrase level annotations and clean isolated instrument audio recordings with minimal leakage or backing track.