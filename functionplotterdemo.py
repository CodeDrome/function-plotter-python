import math

import functionplotter as fp
import samplefunctions as sf


def main():

    print("--------------------")
    print("| codedrome.com    |")
    print("| Function Plotter |")
    print("--------------------\n")

    plot_samples()


def plot_samples():

    fp.plot(functions = [sf.samples["quadratic"]],
            start = -2,
            end = 2,
            step = 0.05,
            config = {"legend_labels": ["quadratic"],
                      "title": "Quadratic",
                      "xlabel": "x",
                      "ylabel": "y",
                      "linewidth": 0.5,
                      "colors": [ "#0000FF" ],
                      "x_limit": (-2.5, 2.5),
                      "y_limit": (-1, 5)
                      })


if __name__ == "__main__":

    main()
