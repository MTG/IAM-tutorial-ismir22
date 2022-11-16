import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from ipywidgets import VBox, Tab, Output
from utils import listen_pattern, pitch_seq_to_cents, myround, pitch_to_cents
from gui_controls import InProcess

class GradeTabPanel(VBox):
    def __init__(self, data, recording, option, pattern_info, all=False):
        super().__init__([InProcess("Processing...")])
        self.data = data
        self.recording = recording
        self.option = option
        self.pattern_info = pattern_info
        self.all_in_one = all

        #self.audio = data[recording]['audio']
        self.annotations = data[recording]['annotations']
        self.freqs = data[self.recording]['pitch_freqs']
        self.times = data[self.recording]['pitch_times']
        self.pitch_hop = data[self.recording]['pitch_hop']
        self.plot_kwargs = data[self.recording]['plot_kwargs']

    def on_show(self):
        # with self.lock:
        if self.all_in_one == True:
            output = Output()
            with output:
                fig, axs = plt.subplots(len(self.pattern_info), 1, figsize=(self.plot_kwargs['figsize'][0], self.plot_kwargs['figsize'][1]*len(self.pattern_info)))
                #fig.subplots_adjust(hspace = .5, wspace=.001)
                axs = axs.ravel()
                for idx, p in enumerate(self.pattern_info):
                    axs = plot_patterns_no_output(p, self.recording, self.option, self.freqs, self.times, self.pitch_hop, self.annotations, self.plot_kwargs, axs, idx)
                plt.show(fig)
            self.children = [output]
        else:
            plotting = plot_patterns(self.recording, self.pattern_info, self.option, self.freqs, self.times, self.pitch_hop, self.annotations, self.plot_kwargs)
            self.children = [plotting]

def create_score_panels(data, recording, option, pattern):
    tab = Tab()
    children = []
    for p in pattern:
        children.append(GradeTabPanel(data, recording, option, p))
    children.append(GradeTabPanel(data, recording, option, pattern, all=True))
    tab.children = children
    count = 0
    for i in range(0, len(pattern)):
        tab.set_title(i, "Pattern instance: %s" % (i))
        count = i
    tab.set_title(count+1, "All together now")

    def on_select(widget):
        tab_idx = widget['new']
        children[tab_idx].on_show()

    tab.observe(on_select, names='selected_index')
    children[0].on_show()
    return [tab]


def plot_patterns(rec, pattern_info, option, freqs, times, pitch_hop, annotations, plot_kwargs):
    sp = pattern_info[0]
    l = pattern_info[1]
    if annotations is not None:
        pat = pattern_info[2]
        pat_full = pattern_info[3]
    else:
        pat = None
        pat_full = None
    fold = pattern_info[-1]
    gr = pattern_info[-3]
    oc = pattern_info[-2]
    this_pitch = freqs[int(max(sp-l,0)):int(sp+2*l)]
    this_times = times[int(max(sp-l,0)):int(sp+2*l)]
    this_mask = this_pitch == 0
    mask = np.full((len(this_pitch),), False)

    tonic = plot_kwargs['tonic']
    p1 = pitch_seq_to_cents(this_pitch, tonic)
    figsize = plot_kwargs['figsize']
    cents = plot_kwargs['cents']
    s_len = len(this_pitch)
    pitch_masked = np.ma.masked_where(mask, p1)
    
    plt.ion()
    output = Output()
    with output:
        fig, ax = plt.subplots(figsize=figsize, nrows=1, ncols=1)
        # hide toolbar and title
        fig.canvas.toolbar_visible = False
        fig.canvas.header_visible = False
        fig.canvas.footer_visible = False
        fig.patch.set_facecolor('white')

        fig.subplots_adjust(wspace=0.3, hspace=0.20, top=0.85, bottom=0.1)
        xlabel = 'Time (s)'
        ylabel = f'Cents Above Tonic of {round(tonic)}Hz' if cents else 'Pitch (Hz)'

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()

        xmin = myround(min(this_times[:s_len]), 5)
        xmax = max(this_times[:s_len])

        sample = pitch_masked.data[:s_len]
        if not set(sample) == {None}:
            ymin_ = min([x for x in sample if x is not None])
            ymin = myround(ymin_, 50)
            ymax = max([x for x in sample if x is not None])
        else:
            ymin=0
            ymax=1000
        
        for s in plot_kwargs['emphasize']:
            assert plot_kwargs['yticks_dict'], \
                "Empasize is for highlighting certain ticks in <yticks_dict>"
            if s in plot_kwargs['yticks_dict']:
                if cents:
                    p_ = pitch_to_cents(plot_kwargs['yticks_dict'][s], plot_kwargs['tonic'])
                else:
                    p_ = plot_kwargs['yticks_dict'][s]
                ax.axhline(p_, color='#db1f1f', linestyle='--', linewidth=1)

        times_samp = this_times[:s_len]
        pitch_masked_samp = pitch_masked[:s_len]

        times_samp = times_samp[:min(len(times_samp), len(pitch_masked_samp))]
        pitch_masked_samp = pitch_masked_samp[:min(len(times_samp), len(pitch_masked_samp))]
        ax.plot(times_samp, pitch_masked_samp, linewidth=0.7)

        if plot_kwargs['yticks_dict']:
            tick_names = list(plot_kwargs['yticks_dict'].keys())
            tick_loc = [pitch_to_cents(p, plot_kwargs['tonic']) if cents else p \
                        for p in plot_kwargs['yticks_dict'].values()]
            ax.set_yticks(tick_loc)
            ax.set_yticklabels(tick_names)
        
        ax.set_xticks(np.arange(xmin, xmax+1, 1))

        plt.xticks(fontsize=8.5)
        ax.set_facecolor('#f2f2f2')

        ax.set_ylim((ymin, ymax))
        ax.set_xlim((xmin, xmax))
            
        x_d = ax.lines[-1].get_xdata()
        y_d = ax.lines[-1].get_ydata()

        x = x_d[int(min(l,sp)):int(l+min(l,sp))]
        y = y_d[int(min(l,sp)):int(l+min(l,sp))]
        
        max_y = ax.get_ylim()[1]
        min_y = ax.get_ylim()[0]
        rect = Rectangle((x_d[int(min(l,sp))], min_y), l*pitch_hop, max_y-min_y, facecolor='lightgrey')
        ax.add_patch(rect)
        
        ax.plot(x, y, linewidth=0.7, color='darkorange')
        ax.axvline(x=x_d[int(min(l,sp))], linestyle="dashed", color='black', linewidth=0.8)

        fig.canvas.draw()
        fig.canvas.flush_events()
        if 'Group' in option:
            if annotations is not None:
                print('This pattern has been identified to match:', pat[0])
                print('The actual pattern in instance is:', pat_full[0])
        listen_pattern(rec, fold, gr, oc, 44100)
        plt.show(fig)
    return output


def plot_patterns_no_output(pattern_info, rec, option, freqs, times, pitch_hop, annotations, plot_kwargs, axes, idx):
    sp = pattern_info[0]
    l = pattern_info[1]
    if annotations is not None:
        pat = pattern_info[2]
        pat_full = pattern_info[3]
    else:
        pat = None
        pat_full = None
    fold = pattern_info[-1]
    gr = pattern_info[-3]
    oc = pattern_info[-2]
    this_pitch = freqs[int(max(sp-l,0)):int(sp+2*l)]
    this_times = times[int(max(sp-l,0)):int(sp+2*l)]
    this_mask = this_pitch == 0
    mask = np.full((len(this_pitch),), False)

    tonic = plot_kwargs['tonic']
    p1 = pitch_seq_to_cents(this_pitch, tonic)
    figsize = plot_kwargs['figsize']
    cents = plot_kwargs['cents']
    s_len = len(this_pitch)
    pitch_masked = np.ma.masked_where(mask, p1)

    #fig.subplots_adjust(wspace=0.3, hspace=0.20, top=0.85, bottom=0.1)
    xlabel = 'Time (s)'
    ylabel = f'Cents Above Tonic of {round(tonic)}Hz' if cents else 'Pitch (Hz)'

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    axes[idx].grid()

    xmin = myround(min(this_times[:s_len]), 5)
    xmax = max(this_times[:s_len])

    sample = pitch_masked.data[:s_len]
    if not set(sample) == {None}:
        ymin_ = min([x for x in sample if x is not None])
        ymin = myround(ymin_, 50)
        ymax = max([x for x in sample if x is not None])
    else:
        ymin=0
        ymax=1000
    
    for s in plot_kwargs['emphasize']:
        assert plot_kwargs['yticks_dict'], \
            "Empasize is for highlighting certain ticks in <yticks_dict>"
        if s in plot_kwargs['yticks_dict']:
            if cents:
                p_ = pitch_to_cents(plot_kwargs['yticks_dict'][s], plot_kwargs['tonic'])
            else:
                p_ = plot_kwargs['yticks_dict'][s]
            axes[idx].axhline(p_, color='#db1f1f', linestyle='--', linewidth=1)

    times_samp = this_times[:s_len]
    pitch_masked_samp = pitch_masked[:s_len]

    times_samp = times_samp[:min(len(times_samp), len(pitch_masked_samp))]
    pitch_masked_samp = pitch_masked_samp[:min(len(times_samp), len(pitch_masked_samp))]
    axes[idx].plot(times_samp, pitch_masked_samp, linewidth=0.7)

    if plot_kwargs['yticks_dict']:
        tick_names = list(plot_kwargs['yticks_dict'].keys())
        tick_loc = [pitch_to_cents(p, plot_kwargs['tonic']) if cents else p \
                    for p in plot_kwargs['yticks_dict'].values()]
        axes[idx].set_yticks(tick_loc)
        axes[idx].set_yticklabels(tick_names)
    
    axes[idx].set_xticks(np.arange(xmin, xmax+1, 1))

    plt.xticks(fontsize=8.5)
    axes[idx].set_facecolor('#f2f2f2')

    axes[idx].set_ylim((ymin, ymax))
    axes[idx].set_xlim((xmin, xmax))
        
    x_d = axes[idx].lines[-1].get_xdata()
    y_d = axes[idx].lines[-1].get_ydata()

    x = x_d[int(min(l,sp)):int(l+min(l,sp))]
    y = y_d[int(min(l,sp)):int(l+min(l,sp))]
    
    max_y = axes[idx].get_ylim()[1]
    min_y = axes[idx].get_ylim()[0]
    rect = Rectangle((x_d[int(min(l,sp))], min_y), l*pitch_hop, max_y-min_y, facecolor='lightgrey')
    axes[idx].add_patch(rect)
    
    axes[idx].plot(x, y, linewidth=0.7, color='darkorange')
    axes[idx].axvline(x=x_d[int(min(l,sp))], linestyle="dashed", color='black', linewidth=0.8)

    if 'Group' in option:
        if annotations is not None:
            axes[idx].set_title('Instance ' + str(idx) + ', identified as: ' + pat[0] + ', annotated as: ' + pat_full[0])
        else:
            axes[idx].set_title('Instance ' + str(idx))
    print('Listen to pattern ' + str(idx) + ':')
    listen_pattern(rec, fold, gr, oc, 44100)
    return axes