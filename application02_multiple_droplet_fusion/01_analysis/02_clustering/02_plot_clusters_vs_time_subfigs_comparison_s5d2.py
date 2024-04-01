#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def main():
    n_steps = 61
    n_chain = 16657

    fig, ax = plt.subplots(2, 1, figsize=(6, 2), constrained_layout=True, sharex=True, sharey=False)


    # =======
    # s_5_d_5
    # =======
    log_fname_0 = "./output_high_density/test_clustering_{0:02d}_frame_{1:05d}.log"
    dat_fname_0 = "./output_high_density/test_clustering_{0:02d}_frame_{1:05d}.dat"

    n_cluster_plot_X = []
    n_cluster_plot_Y = []

    timestep_tmp = 0
    num_cluster = 0
    for i_step in range(n_steps):
        if i_step == 0:
            n_frame = 0
        elif i_step <= 5:
            n_frame = 2500
        else:
            n_frame = 2000
        timestep_tmp += n_frame
        log_fname = log_fname_0.format(i_step, n_frame)
        dat_fname = dat_fname_0.format(i_step, n_frame)

        # read number of clusters
        with open(log_fname, "r") as fin:
            for line in fin:
                if line.startswith("####"):
                    words = line.split()
                    num_cluster = int(words[2])
                    break

        # read cluster labels
        cluster_sizes = [0 for n_c in range(num_cluster)]
        with open(dat_fname, "r") as fin:
            for line in fin:
                if line.startswith("####"):
                    continue
                words = line.split()
                if len(words) < 1:
                    continue
                i_label = int(words[0])
                if i_label > 0:
                    cluster_sizes[i_label - 1] += 1

        # plot a scatter
        X = [timestep_tmp for j in range(num_cluster)]
        if i_step % 2 == 1:
            pass
        else:
            ax[1].scatter(X, cluster_sizes, s=20, c="r", alpha=1.0, linewidths=None)

        n_cluster_plot_X.append(timestep_tmp)
        n_cluster_plot_Y.append(num_cluster)

    ax[0].plot(n_cluster_plot_X, n_cluster_plot_Y, "r--", lw=1.5)


    # =======
    # s_5_d_2
    # =======
    log_fname_0 = "./output_low_density/test_clustering_{0:02d}_frame_{1:05d}.log"
    dat_fname_0 = "./output_low_density/test_clustering_{0:02d}_frame_{1:05d}.dat"

    n_cluster_plot_X = []
    n_cluster_plot_Y = []

    timestep_tmp = 0
    num_cluster = 0
    for i_step in range(n_steps):
        if i_step == 0:
            n_frame = 0
        # elif i_step <= 5:
            # n_frame = 2500
        else:
            n_frame = 2000
        timestep_tmp += n_frame
        log_fname = log_fname_0.format(i_step, n_frame)
        dat_fname = dat_fname_0.format(i_step, n_frame)

        # read number of clusters
        with open(log_fname, "r") as fin:
            for line in fin:
                if line.startswith("####"):
                    words = line.split()
                    num_cluster = int(words[2])
                    break

        # read cluster labels
        cluster_sizes = [0 for n_c in range(num_cluster)]
        with open(dat_fname, "r") as fin:
            for line in fin:
                if line.startswith("####"):
                    continue
                words = line.split()
                if len(words) < 1:
                    continue
                i_label = int(words[0])
                if i_label > 0:
                    cluster_sizes[i_label - 1] += 1

        # plot a scatter
        X = [timestep_tmp for j in range(num_cluster)]
        if i_step % 2 == 1:
            pass
        else:
            ax[1].scatter(X, cluster_sizes, s=16, c="g", alpha=1.0, linewidths=None)

        n_cluster_plot_X.append(timestep_tmp)
        n_cluster_plot_Y.append(num_cluster)

    ax[0].plot(n_cluster_plot_X, n_cluster_plot_Y, "g-.", lw=1.5)



    # other plot settings
    ax[0].set_xticks([20000 * i for i in range(20)])
    ax[0].set_xticklabels([2 * i for i in range(20)], fontsize=12)
    ax[0].set_xlim(-500, 123000)
    ax[1].set_xlabel(r"time step ($\times 10^8$)", fontsize=16)

    ax[0].set_yscale("log")
    # ax[0].set_yticks([10 * i for i in range(6)])
    ax[0].set_yticks([1, 2, 4, 8, 16, 32])
    # ax[0].set_yticklabels([10 * i for i in range(6)], fontsize=12)
    ax[0].set_yticklabels([1, "", 4, "", 16, ""], fontsize=12)
    ax[0].set_ylim(0.6, 63)
    ax[0].set_ylabel(r"$N_{cluster}$", fontsize=16)
    ax[0].grid(True, ls="-", linewidth=0.4, color="gray", alpha=0.5, axis="y")
    ax[0].minorticks_off()

    ax[1].set_yscale("log")
    ax[1].set_yticks([250, 1000, 4000, 16000])
    ax[1].set_yticklabels([250, 1000, 4000, 1600], fontsize=12)
    ax[1].set_ylim(90, 19000)
    ax[1].set_ylabel(r"cluster size", fontsize=16)
    ax[1].grid(True, ls="-", linewidth=0.4, color="gray", alpha=0.5, axis="y")
    ax[1].minorticks_off()


    # ========
    # save fig
    # ========
    figname = "droplet_fusion_s_5_d_5_vs_s_5_d_2_cluster_size_and_number.svg"
    plt.savefig(figname, dpi=150)

if __name__ == '__main__':
    main()
