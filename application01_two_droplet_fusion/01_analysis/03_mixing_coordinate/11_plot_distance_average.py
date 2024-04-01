#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main(i_test):
    n_run = 1

    # load distance data
    dist_array = np.empty((0, 3), float)
    for i_run in range(n_run):
        data_fname = "./test{0}_chain_pairwise_distance_sum_step_{1:02d}.dat".format(i_test, i_run + 1)
        tmp_dist_array = np.loadtxt(data_fname, usecols=(1,2,3))
        dist_array = np.append(dist_array, tmp_dist_array, axis=0)

    # plot
    fig, ax = plt.subplots(1, 1, figsize=(6, 3), constrained_layout=True, sharex=False, sharey=False)
    # X = np.linspace(1, 10000, num=10000, endpoint=True)
    X = np.linspace(1, 1000, num=1000, endpoint=True)
    ax.plot(X, dist_array[:, 0], "r-", lw=1.0)
    ax.plot(X, dist_array[:, 1], "m-", lw=2.0, alpha=0.5)
    ax.plot(X, dist_array[:, 2], "b-", lw=1.0)

    # ax.set_xticks([2000 * i for i in range(11)])
    ax.set_xticks([200 * i for i in range(11)])
    ax.set_xticklabels([2 * i for i in range(11)], fontsize=12)
    # ax.set_xlim(0, 10000)
    ax.set_xlim(0, 1000)
    ax.set_xlabel(r"MD steps ($\times 10^7$)", fontsize=16)

    ax.set_yticks([100 + 50 * i for i in range(11)])
    ax.set_yticklabels([100 + 50 * i for i in range(11)], fontsize=12)
    ax.set_ylim(140, 460)
    ax.set_ylabel(r"m ($\AA$)", fontsize=16)

    fig_name = "test{0}_chain_distance_ave_all.png".format(i_test)
    plt.savefig(fig_name, dpi=150)

if __name__ == '__main__':
    for i_test in [2,3,4,5]:
        main(i_test)
