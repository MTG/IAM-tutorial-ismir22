# Music source separation for Carnatic Music

As seen in the [music segmentation example](music-segmentation), the vocal separation for Carnatic and Hindustani music remains an unsolved (and unexplored!) field. In the [singing voice separation](singing-voice-extraction) walkthrough you can find an example of a model developed specifically to perform vocal separation for Carnatic Music. Let's first introduce the task, the challenges, and current solutions.

## Music source separation
The problem of music source separation (MSS) is aimed at automatically estimating the individual elements in a music mixture. MSS systems, which recently are mostly based on DL architectures, operate on the waveform and on the time-frequency domain, and even on a combination of both. Since this is a core problem in the field of music information research, many efforts to obtain open and high-performance models are done, and several pre-trained systems are made available to be freely used out-of-the-box.

MSS systems are normally trained using the mixture as input, and the target sources as expected output, and the models are optimized to reproduce the same operation. There are few datasets in the literature that may be used for that purpose: musdb18hq, moisesdb, and medleydb. However, these datasets mostly include recordings that can be framed into the pop and rock styles, and therefore, as it normally happens in the field of DL, when training with data belonging in a particular domain, the generalization to out-of-domain use cases is not feasible.

## The problem with Carnatic Music

For the case of Carnatic Music we observe such problem. Not only the available models in the literature do not have any knowledge on this repertoire, but also the task of MSS normally targets the following source setup: _vocals_, _bass_, _drums_, and _other_, and that does not comply with the actual arrangement and nature of Carnatic Music. 

Some well-known models for MSS are Spleeter {cite}`spleeter` by Deezer, Meta's Demucs {cite}`demucs`, and their related extensions and evolutions.

Some efforts have been done on improving separation for Carnatic Music, given the existence of the Saraga dataset {cite}`saraga`, which includes multi-track recordings for Carnatic renditions, although the stems of the different sources are not completely isolated, since the recordings are collected in live performances. Therefore, in the background on the stems, there is leakage or bleeding from the rest of the sources, convoluted by the room response. Some works have been trying to take advantage of these noisy data to use the inherent knowledge in the data, although there is still room for improvement.

See here separation examples of some of these models for Carnatic Music recordings:

- [Deezer's Spleeter](carnatic-separation-spleeter)
- [Leakage-aware cold diffusion model trained on Saraga](carnatic-separation-leakage)
- [Deezer's Spleeter fine-tuned on Saraga](carnatic-separation-spleeter-finetune)
