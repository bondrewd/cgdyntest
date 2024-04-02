# GENESIS cgdyn MD files and analysis scripts

This repository is used to share simulation data for the publication of:
- Jung J, Tan C, and Sugita Y (2023) GENESIS CGDYN: large-scale coarse-grained molecular dynamics simulation with dynamic load balancing for heterogeneous biomolecule systems

## Software

In this work we report the development of GENESIS CGDYN, which can be accessed from:
- GENESIS CGDYN: https://github.com/genesis-release-r-ccs/genesis-2.1.0beta_cgdyn

For MD system preparation and analysis, use the following program:
- GENESIS-cg-tool: https://github.com/genesis-release-r-ccs/genesis_cg_tool

## Directory structure

### Benchmark systems

- `dna_benchmark_hokusai`: benchmark of duplicated DNA system on supercomputer server Hokusai (RIKEN-RCCS) (Supporting Table 1)
- `dna_benchmark`: benchmark of duplicated DNA system on local PC clusters (Supporting Figure 3)
- `dry_martini_benchmark`: benchmark of Martini lipid system on supercoputer Fugaku (Supporting Figure 8a)
- `fugaku_droplet_benchmark/`: benchmark of large-scale protein droplet simulations on supercomputer Fugaku (Supporting Figure 8b)
- `others`: benchmark of previously-reported systems (Tan C _et al._ PLoS Comput Biol, 2022) (Supporting Figure 4)

### Application systems

- `application01_two_droplet_fusion/`: MD simulations of two-droplet fusion system (Figure 3)
- `application02_multiple_droplet_fusion/`: MD simulations of near-realistic-scale multiple-droplet systems (Figure 4)

Analysis scripts are included in each directory.

#### Structures:

##### Application 1: Two droplet system:

- Initial structure: `00_MD/rst/tdp43_1000_minimized.rst` (MD restart file)
- Final structure: `00_MD/output/tdp43_test1_frame10000_with_clustering_labels.cif`
- Intermediate structures: `00_MD/output/tdp43_test1_frame*_with_clustering_labels.cif`


##### Application 2: Multiple droplet system:

