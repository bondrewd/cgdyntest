#!/bin/bash

#PJM -L "rscgrp=small"
#PJM -L "rscunit=rscunit_ft01"
#PJM -L "node=4x2x2"
#PJM --mpi "proc=64"
#PJM -g ra000003
#PJM -x PJM_LLIO_GFSCACHE=/vol0004
#PJM -L "elapse=00:10:59"
#PJM -j
#PJM -S

module switch lang/tcsds-1.2.37

export OMP_NUM_THREADS=12
export PLE_MPI_STD_EMPTYFILE=off

export bindir=/vol0004/ra000003/data/jung_new/program/genesis-mkl-private_nobalance/src/atdyn
illio_transfer ${bindir}/atdyn

mpiexec sh -c 'if [ ${PMIX_RANK} == 0 ]; then ${bindir}/atdyn p64_02.inp > p64_02.out; else ${bindir}/atdyn p64_02.inp; fi'