import numpy as np
import matplotlib.pyplot as plt

def make_plot():
    fig = plt.figure()
    ax = fig.add_subplot(211, autoscale_on=True)
    ax.grid()
    ax.autoscale(enable=True)
    plt.setp(ax.get_xticklabels(), visible=False)
    ax.set_xscale('log')
    ax.set_ylabel('G(t)', fontsize=13)
    
    ax2 = fig.add_subplot(313, autoscale_on=True, sharex=ax)
    ax2.grid()
    ax2.autoscale(enable=True)
    ax2.set_ylabel('Amplitude', fontsize=13)
    ax2.set_xlabel('Correlation time(ms)', fontsize=13)
    
    
    fig.align_ylabels()
    #plt.tight_layout()
    return fig, ax, ax2

def add_data(corrt, G, Gt, corr, modelGt, ax , ax2, datafile, fig):
    ax2.set_ylim([-np.max(G-modelGt), np.max(G-modelGt)])
    line1, = ax.plot(corrt, Gt, '.', lw=0)
    line2, = ax.plot(corr, modelGt, 'r-', lw=2)
    line3, = ax2.plot(corr, G-modelGt, 'b.', lw=0)
    fig.savefig(datafile+'2comp.png')
    plt.close('all')



    
