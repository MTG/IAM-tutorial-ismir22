from ipywidgets import GridspecLayout, Dropdown, Label, Layout

import os
import pickle
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm

from utils import load_json, load_yaml, cents_to_pitch, get_pitch_timestep

import warnings
warnings.filterwarnings("ignore")

class SongChooser(GridspecLayout):
    def __init__(self, update_gui, reset_gui):
        super().__init__(3, 1, height='100px')
        #self.data = data
        self.update_gui = update_gui
        self.reset_gui = reset_gui
        self.data = None
        self.items = self.get_recordings()

        # Instrument
        self.recording = None
        self.style = {'description_width': 'initial'}
        self.recording_menu = Dropdown(
            options=self.items,
            description="Select a recording:",
            style=self.style,
            value=None)
        self.option = None
        self.pattern = None
        self.recording_menu.observe(self.handle_recording_change, names='value')

        # Sample scores
        self.option_menu = Dropdown(options=[], description="Select an option:", style=self.style)
        self.option_menu.observe(self.option_selected, names='value')
        self.option_menu.disabled = True

        # Pattern
        self.pattern_menu = Dropdown(options=[], description="Select a pattern:", style=self.style)
        self.pattern_menu.observe(self.pattern_selected, names='value')
        self.pattern_menu.disabled = True

        self.option_label = Label()
        self.pattern_label = Label()

        self[0, 0] = self.recording_menu
        self[1, 0] = self.option_menu
        self[2, 0] = self.pattern_menu
        #self[2, 0] = self.score_label

    def handle_recording_change(self, change):
        # upload_data.layout.visibility = "visible"
        self.recording = change['new']
        #self.recording = change['new'].split('-')[-1].split('(')[0][1:-1]
        if self.data[self.recording]['annotations'] is not None:
            #option = self.analyser.get_demo_score_list(change['new'])
            option_list = ['by Patterns', 'by Groups']
        else:
            option_list = ['by Groups']
        #self.option_menu.unobserve(self.option_selected, names='value')
        self.option_menu.options = option_list
        self.option_menu.index = None
        self.option_menu.observe(self.handle_option_change, names='value')
        self.option_menu.disabled = False
        self.option_label.value = ""
        self.option_id = None
        (self.reset_gui)()

    def handle_option_change(self, change):
        # upload_data.layout.visibility = "visible"
        self.option = change['new']
        if 'Pattern' in self.option:
            sancara_list = self.data[self.recording]['parsed_patterns']
        else:
            if self.data[self.recording]['annotations'] is not None:
                sancara_list = self.data[self.recording]['groups_with_annotations']
            else:
                sancara_list = self.data[self.recording]['groups']
        self.pattern_menu.unobserve(self.pattern_selected, names='value')
        self.pattern_menu.options = sancara_list
        self.pattern_menu.index = None
        self.pattern_menu.observe(self.pattern_selected, names='value')
        self.pattern_menu.disabled = False
        self.pattern_id = None
        (self.reset_gui)()

    def option_selected(self, change):
        if change['new']:
            self.option = change['new']
            # update filename caption
            self.option_label.value = change['new']
            #(self.update_gui)()

    def pattern_selected(self, change):
        if change['new']:
            self.pattern = change['new']
            # update filename caption
            #self.pattern_label.value = change['new']
            (self.update_gui)()

    def get_recordings(self):
        recordings_dict = load_json(os.path.join(".", "data", "recordings.json"))
        recording_list = list(recordings_dict.keys())
        return recording_list
        #return [self.data[rec]['artists'] + ' - ' + rec + ' (' + self.data[rec]['raga'] + ')' for rec in recording_list]

    @staticmethod
    def get_data():
        recordings_dict = load_json(os.path.join(".", "data", "recordings.json"))
        recording_list = list(recordings_dict.keys())
        for rec in tqdm(recording_list, desc='This process may take a while'):
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
                        'figsize':(15,4)}

                #audio, _ = sf.read(os.path.join(".", "data", rec, "mix.wav"))
                #data[rec]['audio'] = audio
                data['audio'] = os.path.join(".", "data", rec, "mix.wav")
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
                        parsed_patterns[san].append([data_starts[gr][oc], data_lengths[gr][oc], san, None, gr, oc, 'pattern-chunks'])
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
                                groups[gr].append([data_starts[gr][oc], data_lengths[gr][oc], sancara_idx, sancara_idx_full, gr, oc, 'ann-groups-chunks'])
                            else:
                                if sancara_idx_full == []:
                                    sancara_idx_full = ['No data']
                                groups[gr].append([data_starts[gr][oc], data_lengths[gr][oc], ['No match'], sancara_idx_full, gr, oc, 'ann-groups-chunks'])
                    data[rec]['groups_with_annotations'] = groups
                else:
                    data[rec]['parsed_patterns'] = None
                    data[rec]['groups_with_annotations'] = None
                    data[rec]['sancara_list'] = None
                groups_no_pat = {x: [] for x in np.arange(len(data_starts))}
                for gr in np.arange(len(data_starts)):
                    for oc in np.arange(len(data_starts[gr])):
                        groups_no_pat[gr].append([data_starts[gr][oc], data_lengths[gr][oc], gr, oc, 'groups-chunks'])
                data[rec]['groups'] = groups_no_pat
        return data




