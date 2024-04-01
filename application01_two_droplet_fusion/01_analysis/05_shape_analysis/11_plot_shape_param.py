#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main(i_test):
    n_run = 1

    # load distance data
    # shape_array = np.empty((0, 3), float)
    shape_array = np.array([])
    for i_run in range(n_run):
        data_fname = "./test{0}_droplet_shape_step_{1:02d}.dat".format(i_test, i_run + 1)
        tmp_shape_array = np.loadtxt(data_fname, usecols=(1))
        shape_array = np.append(shape_array, tmp_shape_array)

    # plot
    fig, ax = plt.subplots(1, 1, figsize=(6, 3), constrained_layout=True, sharex=False, sharey=False)
    X = np.linspace(1, 10000, num=10000, endpoint=True)

    ax.plot(X, shape_array, "k,", lw=1.0)

    if i_test == 1:
        ax.set_xticks([2000 * i for i in range(11)])
    else:
        ax.set_xticks([200 * i for i in range(11)])
    ax.set_xticklabels([2 * i for i in range(11)], fontsize=12)
    ax.set_xlim(0, 10000)
    ax.set_xlabel(r"MD steps ($\times 10^7$)", fontsize=16)

    ax.set_ylabel(r"$\eta$", fontsize=16)

    fig_name = "test{0}_droplet_shape_all.png".format(i_test)
    plt.savefig(fig_name, dpi=150)

if __name__ == '__main__':
    main(1)
