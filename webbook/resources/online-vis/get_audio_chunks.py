import os
import tqdm
import pickle
import numpy as np
import soundfile as sf
import pandas as pd

from utils import load_json, load_yaml, cents_to_pitch, get_pitch_timestep

recordings_dict = load_json(os.path.join(".", "data", "recordings.json"))
recording_list = list(recordings_dict.keys())
for rec in tqdm.tqdm(recording_list, desc='This process may take a while'):
    # Output
    svara_cent_path = "./data/svara_cents.yaml"
    svara_freq_path = "./data/svara_lookup.yaml"

    svara_cent = load_yaml(svara_cent_path)
    svara_freq = load_yaml(svara_freq_path)

    recordings_dict = load_json("./data/recordings.json")
    recording_list = list(recordings_dict.keys())
    data = {x: {} for x in recording_list}
    for rec in recording_list:
        data[rec]['raga'] = recordings_dict[rec]['raga']
        data[rec]['tonic'] = recordings_dict[rec]['tonic']
        data[rec]['artists'] = recordings_dict[rec]['artist']
        if recordings_dict[rec]['raga'] in svara_freq:
            arohana = svara_freq[recordings_dict[rec]['raga']]['arohana']
            avorahana = svara_freq[recordings_dict[rec]['raga']]['avorahana']
            all_svaras = list(set(arohana+avorahana))
            data[rec]['arohana'] = arohana
            data[rec]['avorahana'] = avorahana

            yticks_dict = {k:cents_to_pitch(v, data[rec]['tonic']) for k,v in svara_cent.items()}
            yticks_dict = {k:v for k,v in yticks_dict.items() if any([x in k for x in all_svaras])}

            data[rec]['plot_kwargs'] = {
                'yticks_dict': yticks_dict,
                'cents':True,
                'tonic': data[rec]['tonic'],
                'emphasize':['S', 'S ', 'S  ', ' S', '  S'],
                'figssize':(15,4)}

        #audio, _ = sf.read(os.path.join(".", "data", rec, "mix.wav"))
        #data[rec]['audio'] = audio
        data['audio'] = os.path.join(".", "data", rec, "mix.wav")
        audio, _ = sf.read(os.path.join(".", "data", rec, "mix.wav"))
        if os.path.exists(os.path.join(".", "data", rec, "annotations_tagged.csv")):
            annotations = pd.read_csv(os.path.join(".", "data", rec, "annotations_tagged.csv"))
            data[rec]['annotations'] = annotations[annotations['tier'].isin(['underlying_full_phrase','underlying_sancara'])]
        else:
            data[rec]['annotations'] = None
        pitch = pd.read_csv(os.path.join(".", "data", rec, "pitch_track.csv"), names=['times', 'freqs'])
        data[rec]['pitch_times'] = pitch['times'].to_numpy()
        pitch_freqs = pitch['freqs'].to_numpy()
        pitch_freqs[pitch_freqs<80] = 0.0
        data[rec]['pitch_freqs'] = pitch_freqs
        data[rec]['pitch_hop'] = np.round(get_pitch_timestep(pitch), 2)

        with open(os.path.join(".", "data", rec, "starts.pkl"), 'rb') as f_starts:
            data_starts = pickle.load(f_starts)
            data[rec]['starts'] = np.array([np.array(xi) for xi in data_starts])
        f_starts.close()

        with open(os.path.join(".", "data", rec, "lengths.pkl"), 'rb') as f_lengths:
            data_lengths = pickle.load(f_lengths)
            data[rec]['lengths'] = np.array([np.array(xi) for xi in data_lengths])
        f_lengths.close()

        if data[rec]['annotations'] is not None:
            group_num = annotations.loc[annotations['match'] == 'match', 'group_num'].to_numpy(dtype=np.int32)
            occ_num = annotations.loc[annotations['match'] == 'match', 'occ_num'].to_numpy(dtype=np.int32)
            sancaras = annotations.loc[annotations['match'] == 'match', 'text'].to_list()
            parsed_patterns = {x: [] for x in np.unique(sancaras)}
            for gr, oc, san in zip(group_num, occ_num, sancaras):
                parsed_patterns[san].append([data_starts[gr][oc], data_lengths[gr][oc], san, None])
                start = int((data_starts[gr][oc] * data[rec]['pitch_hop']) * 44100)
                end = int((data_lengths[gr][oc] * data[rec]['pitch_hop']) * 44100)
                audio_to_save = audio[start:start+end]
                audio_path = os.path.join('.', 'data', rec, 'pattern-chunks', str(gr)+'_'+str(oc)+'.wav')
                sf.write(audio_path, audio_to_save, 44100)
            data[rec]['parsed_patterns'] = parsed_patterns
            data[rec]['sancara_list'] = list(np.unique(annotations['text'].to_numpy()))
            groups = {x: [] for x in np.arange(len(data_starts))}
            sancaras = annotations['text'].to_list()
            for gr in np.arange(len(data_starts)):
                for oc in np.arange(len(data_starts[gr])):
                    sancara_idx = annotations.loc[(annotations['group_num'] == gr) & (annotations['occ_num'] == oc), 'text'].to_list()
                    sancara_idx_full = annotations.loc[(annotations['group_num'] == gr) & (annotations['occ_num'] == oc), 'text_full'].to_list()
                    if sancara_idx:
                        if sancara_idx_full == []:
                            sancara_idx_full = ['No data']
                        groups[gr].append([data_starts[gr][oc], data_lengths[gr][oc], sancara_idx, sancara_idx_full])
                        start = int((data_starts[gr][oc] * data[rec]['pitch_hop']) * 44100)
                        end = int((data_lengths[gr][oc] * data[rec]['pitch_hop']) * 44100)
                        audio_to_save = audio[start:start+end]
                        audio_path = os.path.join('.', 'data', rec, 'ann-groups-chunks', str(gr)+'_'+str(oc)+'.wav')
                        sf.write(audio_path, audio_to_save, 44100)
                    else:
                        if sancara_idx_full == []:
                            sancara_idx_full = ['No data']
                        groups[gr].append([data_starts[gr][oc], data_lengths[gr][oc], ['No match'], sancara_idx_full])
                        start = int((data_starts[gr][oc] * data[rec]['pitch_hop']) * 44100)
                        end = int((data_lengths[gr][oc] * data[rec]['pitch_hop']) * 44100)
                        audio_to_save = audio[start:start+end]
                        audio_path = os.path.join('.', 'data', rec, 'ann-groups-chunks', str(gr)+'_'+str(oc)+'.wav')
                        sf.write(audio_path, audio_to_save, 44100)
            data[rec]['groups_with_annotations'] = groups
        else:
            data[rec]['parsed_patterns'] = None
            data[rec]['groups_with_annotations'] = None
            data[rec]['sancara_list'] = None
        groups_no_pat = {x: [] for x in np.arange(len(data_starts))}
        for gr in np.arange(len(data_starts)):
            for oc in np.arange(len(data_starts[gr])):
                groups_no_pat[gr].append([data_starts[gr][oc], data_lengths[gr][oc]])
                start = int((data_starts[gr][oc] * data[rec]['pitch_hop']) * 44100)
                end = int((data_lengths[gr][oc] * data[rec]['pitch_hop']) * 44100)
                audio_to_save = audio[start:start+end]
                audio_path = os.path.join('.', 'data', rec, 'groups-chunks', str(gr)+'_'+str(oc)+'.wav')
                sf.write(audio_path, audio_to_save, 44100)
        data[rec]['groups'] = groups_no_pat