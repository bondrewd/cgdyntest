#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main(i_test):
    distributions_ts = np.ones((150, 1000, 3))
    fname = "./test{0}_chain_distribution_01.dat".format(i_test)
    i_frame = 0
    i_pos   = 0
    with open(fname, "r") as fin:
        for line in fin:
            if line.startswith("#### BEGIN"):
                continue
            if line.startswith("#### END"):
                i_pos = 0
                i_frame += 1
                continue
            i_pos += 1
            words = line.split()
            distributions_ts[(i_pos + 74) % 150, i_frame, 1] -= int(words[0]) / 30
            distributions_ts[(i_pos + 74) % 150, i_frame, 2] -= int(words[0]) / 30
            distributions_ts[(i_pos + 74) % 150, i_frame, 0] -= int(words[1]) / 30
            distributions_ts[(i_pos + 74) % 150, i_frame, 1] -= int(words[1]) / 30

    # plot...
    # X = np.array([i + 1 for i in range(150)])

    fig, axes = plt.subplots(1, 1, figsize=(10, 2), constrained_layout=True, sharex=False, sharey=False)
    axes.imshow(distributions_ts, aspect=1)

    axes.set_xticks([200 * i for i in range(11)])
    axes.set_xticklabels([2 * i for i in range(11)], fontsize=12)
    axes.set_xlim(0, 1000)
    axes.set_xlabel(r"MD steps ($\times 10^7$)", fontsize=16)

    axes.set_yticks([50 * i for i in range(6)])
    axes.set_yticklabels([500 * i for i in range(6)], fontsize=12)
    axes.set_ylim(0, 150)
    axes.set_ylabel(r"z ($\AA$)", fontsize=16)

    # figname = "test{0}_run01_distribution_timeseries.png".format(i_test)
    figname = "test{0}_run01_distribution_timeseries.svg".format(i_test)
    plt.savefig(figname, dpi=150)

if __name__ == '__main__':
    # i_test = 2
    for i_test in [1,2,3,4,5]:
        main(i_test)
