import math

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def plot(functions, start, end, step, config):

    """
    Plots the functions in Matplotlib with
    values of x between start and end with specified step.
    The config dictionary contains various settings
    for the behaviour and appearance of the plot.
    """

    # set defaults for missing config values
    config["colors"] = config.get("colors", plt.rcParams['axes.prop_cycle'].by_key()['color'])

    config["legend_labels"] = config.get("legend_labels", [*range(1, len(functions) + 1)])

    plt.title(config.get("title", "Title"))
    plt.xlabel(config.get("xlabel", "xlabel"))
    plt.ylabel(config.get("ylabel", "ylabel"))
    plt.xlim(config.get("x_limit", (start, end)))

    if "y_limit" in config:
        plt.ylim(config["y_limit"])

    color_count = len(config["colors"])

    # list of values we apply functions to
    xvalues = np.arange(start, end, step)

    # iterate functions, applying each to x values and plotting result
    for index, function in enumerate(functions):

        yvalues = function(xvalues)

        plt.plot(xvalues,
                 yvalues,
                 linewidth = config.get("linewidth", 1),
                 label = config["legend_labels"][index],
                 color = config["colors"][index % color_count])


    plt.legend()

    plt.show()
