(our-timeline)=
# Post-CompMusic timeline at MTG

In this page we take a look at the work done in the Music Technology Group (MTG) towards the computational analysis of Carnatic and Hindustani Music after the [CompMusic project](https://compmusic.upf.edu/) ended in 2017. After a hiatus of active research in this topic in the research group, a new team was assembled to build new research on top of the efforts done within the context of CompMusic.

Here we summarize the work that has been already done in the form of [conference and journal articles](conf-journal), [software tools](our-software), and we also talk about the [ongoing work](ongoing-work).

(conf-journal)=
## Conference and journal articles

The work done has been divided in two main areas: 

* High-quality **feature extraction** for Carnatic and Hindustani Music.
* Computational musicology research around the characterization and discovery of **melodic patterns**


### Feature extraction: Vocal pitch extraction

* Genís Plaja-Roglans, Thomas Nuttall, Lara Pearson, Xavier Serra, Marius Miron. **Repertoire-specific vocal pitch data generation for improved melodic analysis of Carnatic Music.** Transactions of the International Society for Music Information Retrieval Conf (TISMIR, 2023), [link to paper](https://transactions.ismir.net/articles/10.5334/tismir.137).

### Feature extraction: Singing voice separation

* Genís Plaja-Roglans, Marius Miron, Adithi Shankar, Xavier Serra. **Carnatic singing voice separation using cold diffusion on training data with bleeding.** Proceedings of the 24rd International Society for Music Information Retrieval Conference (ISMIR, 2023), Milan, Italy, [link to paper](http://hdl.handle.net/10230/58188).



### Melodic pattern discovery

* Thomas Nuttall, Genís Plaja, Lara Pearson, Xavier Serra. **The Matrix profile for motif discovery in audio - an example application in Carnatic music.** Proceedings of the 15th International Symposium on Computer Music Multidisciplinary Research (CMMR, 2021), Online, [link to paper](https://repositori.upf.edu/handle/10230/52182?locale-attribute=en).

* Thomas Nuttall, Genís Plaja, Lara Pearson, Xavier Serra. **In Search of Sañcaras: Tradition-Informed Repeated Melodic Pattern Recognition in Carnatic Music.** Proceedings of the 23rd International Society for Music Information Retrieval Conference, (ISMIR, 2022), Bengaluru, India, [link to paper](https://repositori.upf.edu/handle/10230/54155).

* Lara Pearson, Thomas Nuttall, Wim Pouw. **Motif-Gesture Clustering in Karnatak Vocal Performance: A Multimodal Computational Music Analysis.** Proceedings of the 17th International Conference on Music Perception and Cognition, (ICMPC, 2023), link to paper coming soon.


(our-software)=
## Software

In addition to scientific publications and the attached code and demos, we have also worked on software tools and materials that can serve as starting point for researchers to get into the topic of computational analysis of Carnatic and Hindustani Music, but also can be starting point for new research projects and experiments. 

* [compIAM](https://github.com/MTG/compIAM). This is a collaborative effort aimed at being a centralized point where to find tools, models, and datasets for the **comp**utational analysis of **I**ndian **A**rt **M**usic. ``compIAM`` is a pip-installable library that is built on an open source basis, and it could not exist without the contributions of several researchers working on this topic. Currently, ``compIAM`` wraps up more than 10 tools and models for several tasks around melodic, rhythmic, timbre, and structural analysis of Indian Art Music. It also provides standardized access to multiple datasets for diverse problems, and it also provides tools to browse and parse data from the [Dunya database](https://dunya.compmusic.upf.edu/).

* [mirdata](https://github.com/mir-dataset-loaders/mirdata). In fact, access to datasets in ``compIAM`` uses mirdata in the backend. ``mirdata`` is a library aimed at providing standardized and friendly access to the canonical version of music datasets, contributing to a better and more reproducible research in music information.

* **This tutorial.** It was presented in 2022 in within the context of the ISMIR Conference in Bengaluru, India. It provides an overview of the research done towards the computational analysis of Carnatic and Hindustani Music, providing walkthroughs of tools and models using ``compIAM``. It involved several researchers and practitioners around the globe, including musicologists and musicians. After its presentation in the ISMIR Conference, it was also presented as a one-week Workshop in IT Chennai, counting with the participation of 30 students.


(ongoing-work)=
## Ongoing work

Currently, we are also working on several research lines on top of the projects done in the past few years. In this section we review the ongoing efforts and the challenges we need to overcome.

[Saraga](https://mtg.github.io/saraga/) is the largest collection of open data for the computational analysis of Carnatic and Hindustani Music. It comprises audio (including multi-track stems recorded in live performances), manual annotations, and musical and editorial tags. However, this collection has some problems we are trying to overcome:

* **Problem (1). Multi-stem recordings are not isolated.** Since recoded in live performances, the multi-stem recordings are not completely isolated instrument tracks, but have bleeding from the rest of the sources in the background. Therefore, we cannot normally train a source separation model with these data, in order to automatically extract the singing voice or the violin from a rendition.

* **Problem (2). Shortage of melodic pattern annotations.** Saraga includes melodic pattern annotations but the quantity is really far from an acceptable coverage. Also, there is a clear lack of consensus of the relevance of each annotated pattern, making it really difficult to perform a data-driven study or a reliable evaluation.

* **Problem (3). No multi-model data beyond audio.** Saraga has a considerable amount of annotated audio, but no other aligned information of another modality is included. To better understand a musical repertoire, it is important to consider also diverse modalities such like visual cues.

* **Problem (4). Restricted representation of raga and talas.** Although an important number of ragas and talas are represented in the original Saraga dataset, some of these only have a single instance. Additional openly shareable randitions including underrepresented ragas in the dataset could indeed improve the representativeness and research done on top of the dataset.

* **Problem (5). Can we enlarge it to allow of representation learning or other modern approaches to enhance its characterization and understanding?** This is an unexplored idea!

We are currently studying leakage-aware methods to tackle problem **(1)**, exploring also the use of generative methods. We have been working on a Saraga extension to overcome problems **(3)**, **(4)**, and **(5)**. Such extension includes more and cleaner recordings comprising a rich diversity of ragas. We have also compiled **video recordings** aligned with the audio, from which we compute **gesture features**.

For problem **(2)**, although research advances have been done in the past few years, we are currently struggling with the lack of annotations, since annotating melodic motifs is complex and requires expertise. Therefore, although its crucial importance, we are still blocked on addressing these challenge.