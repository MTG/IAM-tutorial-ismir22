(melodic-transcription)=
# Melodic transcription

Efforts to automatically transcribe melodies in Carnatic and Hindustani music have been done {cite}`ranjani_transcription_2017, ranjani_transcription_2019, viraraghavan_transcription_2020`. These approaches show versatile strategies to obtain a descriptive notation for Indian Art Music melodies. These notations are typically reversible and may be used for further research on the performances.

## State Based Transcription (SBT) for Carnatic Music
```{note}
The installation instructions, details of the API and data formats, are available [here](https://www.iitm.ac.in/donlab/preview/music/sbt_cm.html). 
```
The SBT tool extracts the descriptive transcription of a pitch curve of an audio excerpt. The excerpt is typically a segment of a Carnatic rendition. The SBT also needs the excerpt's tonic and its raga as inputs. The descriptive transcription is obtained according to the algorithm described in {cite}`viraraghavan_transcription_2020`, in accordance with the raga's gamaka movements. This output is compact, and is provided as a csv file.

You can interpolate this descriptive transcription to obtain a pitch curve, which is synthesizable. The synthesis quality is insensitive to the interpolation scheme -- linear interpolation is handy to start with. But, do check [this web resource](https://www.iitm.ac.in/donlab/preview/music/CM_manual_synth.html) if you plan to use pitch bend in MIDI.

```{tip}
SBT works better for cleaner recordings, preferably with only a tambura accompaniment.
```
