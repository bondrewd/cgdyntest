#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main(i_test):
    distributions_ts = np.zeros((1000, 150, 2))
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
            distributions_ts[i_frame, (i_pos + 74) % 150, 0] = int(words[0])
            distributions_ts[i_frame, (i_pos + 74) % 150, 1] = int(words[1])

    # plot...
    X = np.array([i + 1 for i in range(150)])
    for j in range(20, 1000, 20):
        fig, axes = plt.subplots(1, 1, figsize=(6, 3), constrained_layout=True, sharex=False, sharey=False)
        y1 = np.average(distributions_ts[j-20:j+20, :, 0], axis=0)
        y2 = np.average(distributions_ts[j-20:j+20, :, 1], axis=0)
        y_sum = y1 + y2
        axes.plot(X, y1, ls="-", c="r", lw=2)
        axes.plot(X, y2, ls="-", c="b", lw=2)
        axes.plot(X, y_sum, ls="--", c="k", lw=1, alpha=0.5)

        axes.set_xticks([30 * i for i in range(6)])
        axes.set_xticklabels([300 * i for i in range(6)], fontsize=12)
        axes.set_xlim(0, 151)
        axes.set_xlabel(r"z ($\AA$)", fontsize=16)

        axes.set_yticks([10 * i for i in range(6)])
        axes.set_yticklabels([10 * i for i in range(6)], fontsize=12)
        axes.set_ylim(0, 45)
        axes.set_ylabel("count", fontsize=16)

        figname = "_test{0}_run01_frame_{1:04d}_distribution.svg".format(i_test, j)
        plt.savefig(figname, dpi=150, transparent=False)

if __name__ == '__main__':
    i_test = 1
    main(i_test)
