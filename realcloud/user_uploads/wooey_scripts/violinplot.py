# -*- coding: utf-8 -*-
__author__ = 'xujm@realbio.cn'
import argparse
import logging
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

matplotlib.use('Agg')

parser = argparse.ArgumentParser(description="A violin plot plays a similar role as a box and whisker plot. It shows the\
distribution of quantitative data across several levels of one (or more) categorical variables such that those \
distributions can be compared. Unlike a box plot, in which all of the plot components correspond to actual \
datapoints, the violin plot features a kernel density estimation of the underlying distribution.")
parser.add_argument('--table', dest='table', type=argparse.FileType('r'), required=True, help='Data table for plotting')
group1 = parser.add_argument_group('group1', 'group1 description')
group1.add_argument('--split', action='store_true', dest='split',
                    help="split violins to compare the across the hue variable")
parser.add_argument('--verbose', action='store_true', dest='verbose', help='Enable debug info')
parser.add_argument('--version', action='version', version='1.0')

if __name__ == '__main__':
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s]%(name)s:%(levelname)s:%(message)s",
            filename='debug.log'
        )

    F_table = args.table
    O_vio = "vio.png"
    d = {}
    content = F_table.readlines()
    l_header = content[0].rstrip().split("\t")
    for i in l_header:
        d[i] = []
    for line in content[1:]:
        fields = line.rstrip().split("\t")
        d[l_header[0]].append(float(fields[0]))
        d[l_header[1]].append(fields[1])
        d[l_header[2]].append(fields[2])

    tips = pd.DataFrame(d)
    sns.set(style="ticks", palette="pastel", color_codes=True)
    plt.subplots(figsize=(12, 6))
    dx = sns.violinplot(y="tax", x="Relative abundance", hue="Group", scale="width", data=tips, split=args.split,
                        inner="quart",
                        palette={"Health": sns.xkcd_rgb["peach"], "Carries": sns.xkcd_rgb["baby blue"]})
    sns.despine()
    plt.savefig(O_vio)
