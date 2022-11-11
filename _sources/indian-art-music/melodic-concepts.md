# Carnatic Melodic Concepts
## Rāga and rāga bhāva
The melodic frameworks on which Carnatic music is based are known as rāgas. One of the main aesthetic goals of Carnatic performance is the correct expression of rāga. Rāgas can be understood as collections of phrases or melodies, comprising gamakas (ornamentation) and svaras (notes) that are considered part of the melodic framework, and performed in ways that follow the grammar of the rāga. 

Each rāga has its own character or mood, referred to as rāga bhāva. Rāga bhāva cannot be adequately described using words such as simple emotion terms, but it can be experienced when listening to or performing a rāga.

## Svara
Svaras are note-length units with theoretical pitch positions, and are referred to using sargam syllables – sa ri ga ma pa dha and ni. Sargam syllables are used in written notation, and also in certain musical formats when the svara names are sung. 

In practice, most svaras are performed with gamakas (ornamentation), rather than as plain notes {cite}`ramanathan_sargam_2004`. Therefore, although svaras are often referred to using the English term ‘notes’, they differ from notes in that the gamakas with which they are performed are considered integral to the svara {cite}`viswanathan_analysis_1977`. 

## Gamaka
Many rāgas involve heavy use of gamakas (ornamentation) such as oscillations, slides and flicks to other pitches. Although gamaka typologies can be found in musical treatises, in practice, gamakas tend to evade categorisation due to the many subtle variations found in performance {cite}`viswanathan_analysis_1977`. Nevertheless, such typologies can provide some idea of the range of gamakas performed, as can be seen in [this webpage](https://saayujya.com/index.php/2019/12/03/gamaka-notation/) based on a gamaka typology from the **Saṅgīta-sampradāya-pradarśini**] {cite}`diksitar_sangita_2008`, which draws on [original work by Gopala Krishna Koduri](https://freesound.org/people/gopalkoduri/packs/9949/).

It’s important to note that gamakas are not superficial decoration but rather are integral to musical meaning {cite}`viswanathan_analysis_1977`. For example, when two rāgas have the same svaras, it is often the gamakas used that disambiguate the rāgas {cite}`kassebaum_karnatak_2000`.
 
Gamakas, can greatly alter the sound of the notated svaras (notes); for example, some gamakas do not rest at all on the theoretical pitch of the notated svara, and instead involve oscillations between pitches either side of it {cite}`krishna_carnatic_2012`, as seen in {numref}`pitch_plot_mgmpmmgrg`.


```{figure} ../images/pitch_plot.png
---
alt: Pitch plot mgmpmmgrg
name: pitch_plot_mgmpmmgrg
---
Pitch movement for the sañcāra ‘mgmpmmgrg’ from the recording of Koti Janmani in rāga rītigauḷa, performed by the Akkarai Sisters. It can be seen that the long ga at the end of the phrase is performed as an oscillation between ri and ma, which is typical for this rāga.
```

This oscillatory movement is particularly characteristic of the Carnatic style, and can often subsume individual svaras {cite}`pearson_coarticulation_2016`. The surface effect on the melodic line is that it typically has fewer stable pitch regions than many other styles, as seen in {numref}`pitch_plot_mgmpmmgrg`. Such qualities makes it impossible for researchers who are not themselves Carnatic musicians to reliably identify svaras from audio recordings. Recent work has attempted to automate this task by creating descriptive transcriptions that assign svara names to key points in the melodic flow {cite}`ranjani_transcription_2017, ranjani_transcription_2019, viraraghavan_transcription_2020`. However, such descriptive transcriptions do not necessarily align with the underlying svaras that musicians would use to notate the phrase, which may or may not be a problem, depending on the research question and purpose of the transcription. 

> **Implications for MIR:**
> The heavy use of gamakas, especially oscillations, makes automated transcription of Carnatic music a challenging task. 

## Sañcāra
Another important feature of the style is the structural and expressive significance of motifs and phrases known as sañcāras, which can be defined as coherent segments of melodic movement that follow the grammar of the rāga {cite}`viswanathan_analysis_1977, pesch_oxford_2009`. The term sañcāra comes from the Sanskrit root सञ्चर्, meaning to move. Although occasionally the term might be used to refer to phrases that are particularly characteristic of a rāga, the more common use of the term is in reference to any melodic segment that is coherent from a Carnatic music perspective. 

These melodic patterns are the means through which the character of the rāga is expressed and they form the basis of various improvisatory and compositional formats in the style {cite}`viswanathan_analysis_1977, ishwar_patterns_2013`. There are no definitive lists of all possible sañcāras in each rāga, rather the body of existing compositions and the living oral tradition of rāga performance act as repositories for that knowledge. 

> **Implications for MIR:** Sañcāras are the building blocks of Carnatic music, and so there is considerable musicological interest in searching for them. However,
> as is the case with the related concept of ‘musical phrase’, there may be ambiguity regarding the borders of the sañcāra: for example, different annotators may
> segment at different hierarchical levels (for a related discussion in the context of Western popular music, see {cite}`bruderer_perception_2009`).

## Characteristic phrases or piḍis
These are phrases that can only be found in one rāga, and thus point clearly to that rāga. As explained by the Carnatic musician and musicologist, T. Viswanathan, “Each rāga has its own characteristic phrases which appear regularly in compositions, and which are guaranteed to produce instant recognition (and, if well performed, appreciation) in the audience” ({cite}`viswanathan_analysis_1977`, p. 38).

> **Implications for MIR:**
> Many rāgas will be identifiable from key characteristic motifs (piḍis).

## Tambūrā drone
The tambūrā creates a plucked drone, which includes sa (ṣaḍja) and usually pa (pañcama), the perfect fifth above (although in some rāgas, ma might be used as the other tone). Sa is set to the pitch in which the singer/instrumentalist feels most comfortable performing.  
The ṣaḍja (sa) has a ‘tonic-like’ effect, where we feel a sense of rest on that tone, and hence it is sometimes referred to by musicologists as the ‘tonic’, even though no such term exists in Carnatic music. 

> **Implications for MIR:**
> sa can be placed at any pitch, and usually remains the same throughout a performance. However a few rāgas may be presented in the madhyama śruti, which shifts the
> position of sa. The fact that sa may be placed at any pitch means that for many MIR processes, pitch needs to be normalized to wherever sa is placed.  