from __future__ import division
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator

mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 1.0
mpl.rcParams['xtick.minor.size'] = 5
mpl.rcParams['xtick.minor.width'] = 1.0
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 1.0
mpl.rcParams['ytick.minor.size'] = 5
mpl.rcParams['ytick.minor.width'] = 1.0

def add_minorticks(xfreq=2, yfreq=2):
    ax = plt.gca()
    ax.minorticks_on()
    xticks = ax.xaxis.get_majorticklocs()
    yticks = ax.yaxis.get_majorticklocs()
    dx = xticks[1] - xticks[0]
    dy = yticks[1] - yticks[0]
    xminorLocator = MultipleLocator(dx/xfreq)
    yminorLocator = MultipleLocator(dy/yfreq)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
