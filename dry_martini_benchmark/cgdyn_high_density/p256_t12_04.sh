#!/bin/bash

#PJM -L "rscgrp=large"
#PJM -L "rscunit=rscunit_ft01"
#PJM -L "node=8x8x8:strict"
#PJM --mpi "proc=2048"
#PJM -g ra000003
#PJM -x PJM_LLIO_GFSCACHE=/vol0004
#PJM -L "elapse=00:10:59"
#PJM -j
#PJM -S

module switch lang/tcsds-1.2.37

export OMP_NUM_THREADS=12
export PLE_MPI_STD_EMPTYFILE=off

export bindir=/vol0004/ra000003/data/jung_new/program/genesis-mkl-private_cgdyn_martini_omp/src/cgdyn
llio_transfer ${bindir}/cgdyn

mpiexec -np 256 sh -c 'if [ ${PMIX_RANK} == 0 ]; then ${bindir}/cgdyn p256_t12_04.inp > p256_t12_04.out; else ${bindir}/cgdyn p256_t12_04.inp; fi'

