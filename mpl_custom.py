from __future__ import division

from matplotlib import rcParams
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from cycler import cycler

#colorbrewer2 Dark2 qualitative color table
dark2_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

default_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def get_colors():
    return dark2_colors

def customize_mpl(custom_colors=True):
    """Tweak matplotlib visual style"""
    rcParams['xtick.major.size'] = 10
    rcParams['xtick.major.width'] = 1.0
    rcParams['xtick.minor.size'] = 5
    rcParams['xtick.minor.width'] = 1.0
    rcParams['ytick.major.size'] = 10
    rcParams['ytick.major.width'] = 1.0
    rcParams['ytick.minor.size'] = 5
    rcParams['ytick.minor.width'] = 1.0
    rcParams['axes.linewidth'] = 2.0
    rcParams['axes.labelsize'] = 20
    if custom_colors:
        cyc = ( cycler('color', dark2_colors) +
            cycler('linestyle', ['-', '--', ':', '-.', '-', '--', ':', '-.']) )
        plt.rc('axes', prop_cycle=cyc)
    rcParams['xtick.labelsize'] = 'large'
    rcParams['ytick.labelsize'] = 'large'
    rcParams['figure.figsize'] = (8.0, 6.0)
    rcParams['figure.dpi'] = 150
    rcParams['savefig.dpi'] = 150
    rcParams['savefig.bbox'] = 'tight'
    rcParams['lines.linewidth'] = 2
    rcParams['legend.borderaxespad'] = 1.75

def add_minorticks(ax=None, xfreq=2, yfreq=2):
    """
    Add <xfreq> and <yfreq> minor ticks per x- and y-axis major ticks,
    counting the minor ticks that would be hidden behind the major ticks
    """
    if not ax:
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

def long_ticks(length=10.0, width=1.0):
    rcParams['xtick.major.size'] = length
    rcParams['xtick.major.width'] = width
    rcParams['xtick.minor.size'] = length / 2.0
    rcParams['xtick.minor.width'] = width
    rcParams['ytick.major.size'] = length
    rcParams['ytick.major.width'] = width
    rcParams['ytick.minor.size'] = length / 2.0
    rcParams['ytick.minor.width'] = width

def thick_borders(thickness=2.0):
    rcParams['axes.linewidth'] = thickness

def thick_lines(thickness=2.0):
    rcParams['lines.linewidth'] = thickness

def hi_res(res=150):
    rcParams['figure.dpi'] = res
    rcParams['savefig.dpi'] = res

def use_dark2_colors(dashes=False):
    if dashes:
        linestyle = ['-', '--', ':', '-.', '-', '--', ':', '-.']
    else:
        linestyle = ['-'] * 8
    cyc = ( cycler('color', dark2_colors) + cycler('linestyle', linestyle) )
    plt.rc('axes', prop_cycle=cyc)

def use_default_colors(dashes=False):
    if dashes:
        linestyle = ['-', '--', ':', '-.', '-', '--', ':']
    else:
        linestyle = ['-'] * 7
    cyc = ( cycler('color', default_colors) + cycler('linestyle', linestyle) )
    plt.rc('axes', prop_cycle=cyc)

def set_linestyle(linestyle=['-', '--', ':', '-.']):
    color = default_colors[:len(linestyle)]
    cyc = ( cycler('color', color) + cycler('linestyle', linestyle) )
    plt.rc('axes', prop_cycle=cyc)

