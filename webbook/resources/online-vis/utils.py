import os
import json
import math
import yaml
import numpy as np
from IPython.display import Audio
from IPython.display import display

import essentia.standard as estd

def load_tonic(path):
    """
    Load yaml at <path> to dictionary, d
    
    Returns
    =======
    Wrapper dictionary, D where
    D = {filename: d}
    """
    if not os.path.isfile(path):
        return None
    with open(path) as f:
        d = float(f.readline())   
    return d

def load_yaml(path):
    """
    Load yaml at <path> to dictionary, d
    
    Returns
    =======
    Wrapper dictionary, D where
    D = {filename: d}
    """
    if not os.path.isfile(path):
        return None
    with open(path) as f:
        d = yaml.load(f, Loader=yaml.FullLoader)   
    return d

def load_json(path):
    """
    Load yaml at <path> to dictionary, d
    
    Returns
    =======
    Wrapper dictionary, D where
    D = {filename: d}
    """
    if not os.path.isfile(path):
        return None
    with open(path) as f:
        d = json.load(f)   
    return d


#### VISUALISATION UTILS

def pitch_to_cents(p, tonic):
    """
    Convert pitch value, <p> to cents above <tonic>.
    :param p: Pitch value in Hz
    :type p: float
    :param tonic: Tonic value in Hz
    :type tonic: float
    :return: Pitch value, <p> in cents above <tonic>
    :rtype: float
    """
    return 1200*math.log(p/tonic, 2) if p else None

def cents_to_pitch(c, tonic):
    """
    Convert cents value, <c> to pitch in Hz
    :param c: Pitch value in cents above <tonic>
    :type c: float/int
    :param tonic: Tonic value in Hz
    :type tonic: float
    :return: Pitch value, <c> in Hz 
    :rtype: float
    """
    return (2**(c/1200))*tonic

def pitch_seq_to_cents(pseq, tonic):
    """
    Convert sequence of pitch values to sequence of 
    cents above <tonic> values
    :param pseq: Array of pitch values in Hz
    :type pseq: np.array
    :param tonic: Tonic value in Hz
    :type tonic: float
    :return: Sequence of original pitch value in cents above <tonic>
    :rtype: np.array
    """
    return np.vectorize(lambda y: pitch_to_cents(y, tonic))(pseq)

####### LISTENING UTILS

#def listen_pattern(audio, sp, l, sr, pitch_hop):
#    sp_time = sp * pitch_hop
#    l_time = l * pitch_hop
#    #audio_to_play = estd.EasyLoader(filename=audio, startTime=sp_time, endTime=l_time, downmix='mix')()
#    audio_to_play = 
#    display(Audio(audio_to_play, rate=sr))
def listen_pattern(rec, fold, gr, oc, sr):
    audio_path = os.path.join('.', 'data', rec, fold, str(gr)+'_'+str(oc)+'.wav')
    audio = estd.MonoLoader(filename=audio_path)()
    display(Audio(audio, rate=sr))

####### MISC UTILS

def myround(x, base=5):
    return base * round(x/base)

def get_pitch_timestep(pitch):
    return pitch['times'].iat[1] - pitch['times'].iat[0]


########## FANCY PROGRESS BAR (extracted from https://github.com/kuk/log-progress)
def log_progress(sequence, every=None, size=None, name='Loaded recodings'):
    from ipywidgets import IntProgress, HTML, VBox
    from IPython.display import display

    is_iterator = False
    if size is None:
        try:
            size = len(sequence)
        except TypeError:
            is_iterator = True
    if size is not None:
        if every is None:
            if size <= 200:
                every = 1
            else:
                every = int(size / 200)     # every 0.5%
    else:
        assert every is not None, 'sequence is iterator, set every'

    if is_iterator:
        progress = IntProgress(min=0, max=1, value=1)
        progress.bar_style = 'info'
    else:
        progress = IntProgress(min=0, max=size, value=0)
    label = HTML()
    box = VBox(children=[label, progress])
    display(box)

    index = 0
    try:
        for index, record in enumerate(sequence, 1):
            if index == 1 or index % every == 0:
                if is_iterator:
                    label.value = '{name}: {index} / ?'.format(
                        name=name,
                        index=index)
                else:
                    progress.value = index
                    label.value = u'{name}: {index} / {size}'.format(
                        name=name,
                        index=index,
                        size=size)
            yield record
    except:
        progress.bar_style = 'danger'
        raise
    else:
        progress.bar_style = 'success'
        progress.value = index
        label.value = "{name}: {index}".format(
            name=name,
            index=str(index or '?'))

