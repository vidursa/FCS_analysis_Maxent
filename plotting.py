import numpy as np
import matplotlib.pyplot as plt

def make_plot():
    fig = plt.figure()
    ax = fig.add_subplot(211, autoscale_on=True)
    ax.grid()
    ax.autoscale(enable=True)
    plt.setp(ax.get_xticklabels(), visible=False)
    
    ax2 = fig.add_subplot(413, autoscale_on=True, sharex=ax)
    ax2.grid()
    ax2.autoscale(enable=True)
    plt.setp(ax2.get_xticklabels(), visible=False)
    
    ax3 = fig.add_subplot(414, autoscale_on=True, sharex=ax)
    ax3.grid()
    #ax3.autoscale(enable=True)
    
    ax.set_xscale('log')
    #ax.set_xlabel('Correlation time(ms)', fontsize=9)
    ax.set_ylabel('G(t)', fontsize=13)
    
    #ax2.set_xscale('log')
    #ax2.set_ylim([-0.05, 1.1])
    ax2.set_ylabel('Amplitude', fontsize=13)
    #ax2.set_xlabel('Correlation time(ms)', fontsize=9)

    #ax3.set_xscale('log')
    ax3.set_ylim([-0.0025, 0.0025])
    ax3.set_ylabel('Residual', fontsize=13)
    ax3.set_xlabel('Correlation time(ms)', fontsize=13)
    fig.align_ylabels()
    plt.tight_layout()
    return fig, ax, ax2, ax3

def add_data(ta, a, corrt, G, Gt, corr, modelGt, ax , ax2, ax3, datafile, fig):
    ax3.set_ylim([-np.max(G-modelGt), np.max(G-modelGt)])
    line1, = ax.plot(corrt, Gt, '.', lw=0)
    line2, = ax.plot(corr, modelGt, 'r-', lw=2)
    line3, = ax2.plot(ta[1:], a[1:], 'b.', lw=0)
    line4, = ax3.plot(corr, G-modelGt, 'b.', lw=0)
    fig.savefig(datafile+'maxent1.png')
    plt.close('all')



    
