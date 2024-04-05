#!/bin/bash

#PJM -L "rscgrp=small"
#PJM -L "rscunit=rscunit_ft01"
#PJM -L "node=4x2x2"
#PJM --mpi "proc=256"
#PJM -g ra000003
#PJM -x PJM_LLIO_GFSCACHE=/vol0004
#PJM -L "elapse=00:10:59"
#PJM -j
#PJM -S

module switch lang/tcsds-1.2.37

export OMP_NUM_THREADS=3
export PLE_MPI_STD_EMPTYFILE=off

export bindir=/vol0004/ra000003/data/jung_new/program/genesis-mkl-private_nobalance/src/cgdyn
illio_transfer ${bindir}/cgdyn

mpiexec sh -c 'if [ ${PMIX_RANK} == 0 ]; then ${bindir}/cgdyn p256_t3_05.inp > p256_t3_05.out; else ${bindir}/cgdyn p256_t3_05.inp; fi'
