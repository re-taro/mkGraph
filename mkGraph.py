from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter
from pylab import *
import warnings


plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

def make_graph(graphs, xlabel, ylabel, range, fileName, legend = True, grid = True, show = False, capsize = 3, xscale_log = False, yscale_log = False, dpi = 300):
    fig, ax = plt.subplots(figsize = (7, 4))

    for datas in graphs:
        if datas["type"] == "errory":
            ax.errorbar(datas["x"], datas["y"], yerr = datas["yerr"], marker = datas["marker"], color = datas["color"], label = datas["label"], capsize = datas["capsize"], linestyle = datas["linestyle"])
        elif datas["type"] == "errorx":
            ax.errorbar(datas["x"], datas["y"], xerr = datas["xerr"], marker = datas["marker"], color = datas["color"], label = datas["label"], capsize = capsize, linestyle = datas["linestyle"])
        elif datas["type"] == "errorxy":
            ax.errorbar(datas["x"], datas["y"], xerr = datas["xerr"], yerr = datas["yerr"], marker = datas["marker"], color = datas["color"], label = datas["label"], capsize = capsize, linestyle = datas["linestyle"])
        elif datas["type"] == "plot":
            ax.plot(datas["x"], datas["y"], marker = datas["marker"], color = datas["color"], label = datas["label"], linestyle = datas["linestyle"])
        elif datas["type"] == "scatter":
            ax.scatter(datas["x"], datas["y"], marker = datas["marker"], color = datas["color"], label = datas["label"])
        else:
            warnings.warn("wrong type")

    if xscale_log:
        ax.set_xscale("log")
    if yscale_log:
        ax.set_yscale("log")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if legend:
        plt.legend()

    xmax, ymax, xmin, ymin = range["xmax"], range["ymax"], range["xmin"], range["ymin"]
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    if grid:
        ax.grid(True)
        if not xscale_log:
            ax.xaxis.set_major_locator(MultipleLocator((xmax-xmin)/5))
            ax.xaxis.set_minor_locator(MultipleLocator((xmax-xmin)/25))
        if not yscale_log:
            ax.yaxis.set_major_locator(MultipleLocator((ymax-ymin)/5))
            ax.yaxis.set_minor_locator(MultipleLocator((ymax-ymin)/25))
            ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))

    if show:
        plt.show()

    fileName += ".jpg"
    plt.savefig(fileName,format="jpg",dpi=dpi)
    print(f"saved as {fileName}")