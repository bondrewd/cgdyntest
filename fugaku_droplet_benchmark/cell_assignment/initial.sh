#!/bin/bash -f
#$ -cwd
#$ -q q3.q
#$ -pe impi32 64
#$ -S /bin/bash

#. /home/mdsoft/mpi-selector/data/ib-openmpi-4.1.0_intel-2020.4_cuda-11.3_goby.sh
program="/home/jung/goby/program/genesis-mkl-private_assignment/src/cgdyn/cgdyn"

export OMP_NUM_THREADS=1
export I_MPI_FABRICS=shm:ofi

#mpirun -machinefile $TMP/machines -npernode 32 -n 64 ${program} p64.inp > p64.out
mpiexec.hydra -f $TMP/machines -genv OMP_NUM_THREADS=$OMP_NUM_THREADS -genv I_MPI_FABRICS=shm:ofi -np 64 -ppn 32 ${program} initial.inp > initial.out
