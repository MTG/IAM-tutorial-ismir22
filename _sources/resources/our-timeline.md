(our-timeline)=
# Post-CompMusic timeline at MTG

In this page we take a look at the work done in the Music Technology Group towards the computational analysis of Carnatic and Hindustani Music after the CompMusic project ended in 2017. After a hiatus of active research in this topic in the research group, a new team was assembled to build new research on top of the efforts done within the context of CompMusic.


## Conference and journal articles

The work done has been divided in two main areas: 

* High-quality **feature extraction** for Carnatic and Hindustani Music.
* Computational musicology research around the characterization and discovery of **melodic patterns**


### Feature extraction: Vocal pitch extraction

* Genís Plaja-Roglans, Thomas Nuttall, Lara Pearson, Xavier Serra, Marius Miron. "Repertoire-specific vocal pitch data generation for improved melodic analysis of Carnatic Music." Transaction of the Int. Society for Music Information Retrieval Conf (TISMIR, 2023), [link to paper](https://transactions.ismir.net/articles/10.5334/tismir.137).

### Feature extraction: Singing voice separation

* Genís Plaja-Roglans, Marius Miron, Adithi Shankar, Xavier Serra. "Carnatic singing voice separation using cold diffusion on training data with bleeding." Proc. of the 24rd Int. Society for Music Information Retrieval Conference (ISMIR, 2023), Milan, Italy, [link to paper](http://hdl.handle.net/10230/58188).



### Melodic pattern discovery

* Thomas Nuttall, Genís Plaja, Lara Pearson, Xavier Serra. "The Matrix profile for motif discovery in audio - an example application in Carnatic music." Proceedings of the 15th International Symposium on Computer Music Multidisciplinary Research (CMMR, 2021), Online, [link to paper](https://repositori.upf.edu/handle/10230/52182?locale-attribute=en).

* Thomas Nuttall, Genís Plaja, Lara Pearson, Xavier Serra. "In Search of Sañcaras: Tradition-Informed Repeated Melodic Pattern Recognition in Carnatic Music." Proceedings of the 23rd International Society for Music Information Retrieval Conference, (ISMIR, 2022), Bengaluru, India, [link to paper](https://repositori.upf.edu/handle/10230/54155).

* Lara Pearson, Thomas Nuttall, Wim Pouw. "Motif-Gesture Clustering in Karnatak Vocal Performance: A Multimodal Computational Music Analysis". Proceedings of the 17th International Conference on Music Perception and Cognition, (ICMPC, 2023), link to paper coming soon.



## Software

In addition to scientific publications and the attached code and demos, we have also worked on software tools and materials that can serve as starting point for researchers to get into the topic of computational analysis of Carnatic and Hindustani Music, but also can be starting point for new research projects and experiments. 

* [compIAM](https://github.com/MTG/compIAM). This is a collaborative effort aimed at being a centralized point where to find tools, models, and datasets for the **comp**utational analysis of **I**ndian **A**rt **M**usic. ``compIAM`` is a pip-installable library that is built on an open source basis, and it could not exist without the contributions of several researchers working on this topic. Currently, ``compIAM`` wraps up more than 10 tools and models for several tasks around melodic, rhythmic, timbre, and structural analysis of Indian Art Music. It also provides standardized access to multiple datasets for diverse problems, and it also provides tools to browse and parse data from the [Dunya database](https://dunya.compmusic.upf.edu/).

* [mirdata](https://github.com/mir-dataset-loaders/mirdata). In fact, access to datasets in ``compIAM`` uses mirdata in the backend. ``mirdata`` is a library aimed at providing standardized and friendly access to the canonical version of music datasets, contributing to a better and more reproducible research in music information.

* **This tutorial!** It was presented in 2022 in within the context of the ISMIR Conference in Bengaluru, India. It provides an overview of the research done towards the computational analysis of Carnatic and Hindustani Music, providing walkthroughs of tools and models using ``compIAM``. It involved several researchers and practitioners around the globe, including musicologists and musicians. After its presentation in the ISMIR Conference, it was also presented as a one-week Workshop in IT Chennai, counting with the participation of 30 students.