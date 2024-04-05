#!/bin/bash

#PJM -L "rscgrp=small"
#PJM -L "rscunit=rscunit_ft01"
#PJM -L "node=1"
#PJM --mpi "proc=4"
#PJM -g ra000003
#PJM -x PJM_LLIO_GFSCACHE=/vol0004
#PJM -L "elapse=00:40:59"
#PJM -j
#PJM -S

module switch lang/tcsds-1.2.37

export OMP_NUM_THREADS=12
export PLE_MPI_STD_EMPTYFILE=off

export bindir=/vol0004/ra000003/data/jung_new/program/genesis-mkl-private_nobalance/src/atdyn
illio_transfer ${bindir}/atdyn

mpiexec sh -c 'if [ ${PMIX_RANK} == 0 ]; then ${bindir}/atdyn p4_05.inp > p4_05.out; else ${bindir}/atdyn p4_05.inp; fi'
