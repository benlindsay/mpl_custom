from __future__ import division

from matplotlib import rcParams
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#colorbrewer2 Dark2 qualitative color table
dark2_colors = [(0.10588235294117647, 0.6196078431372549, 0.4666666666666667),
                (0.8509803921568627, 0.37254901960784315, 0.00784313725490196),
                (0.4588235294117647, 0.4392156862745098, 0.7019607843137254),
                (0.9058823529411765, 0.1607843137254902, 0.5411764705882353),
                (0.4, 0.6509803921568628, 0.11764705882352941),
                (0.9019607843137255, 0.6705882352941176, 0.00784313725490196),
                (0.6509803921568628, 0.4627450980392157, 0.11372549019607843),
                (0.4, 0.4, 0.4)]

def get_colors():
    return dark2_colors

def customize_mpl(customColors=True):
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
    if customColors:
        rcParams['axes.color_cycle'] = dark2_colors
    rcParams['xtick.labelsize'] = 'large'
    rcParams['ytick.labelsize'] = 'large'
    rcParams['figure.figsize'] = (8.0, 6.0)
    rcParams['figure.dpi'] = 120
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
