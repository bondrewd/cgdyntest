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

export CVERSION=1.2.34
export OMP_NUM_THREADS=12
export PLE_MPI_STD_EMPTYFILE=off
export FLIB_FASTOMP=FALSE
export FLIB_CNTL_BARRIER_ERR=FALSE

. /vol0004/apps/oss/spack/share/spack/setup-env.sh
spack load gromacs@2023.1

THDA=close
THDS=$OMP_NUM_THREADS

export XOS_MMM_L_PAGING_POLICY=demand:demand:demand
export XOS_MMM_L_ARENA_LOCK_TYPE=0
if [ $THDA = "scatter" ]; then
  export GOMP_CPU_AFFINITY="12-48:12 13-49:12 14-50:12 15-51:12 16-52:12 17-53:12 18-54:12 19-55:12 20-56:12 21-57:12 22-58:12 23-59:12"
elif [ $THDA = "compact" ]; then
  cmg0=$(($THDS/4+11))
  cmg1=$(($THDS/4+23))
  cmg2=$(($THDS/4+35))
  cmg3=$(($THDS/4+47))
  export GOMP_CPU_AFFINITY="12-$cmg0 24-$cmg1 36-$cmg2 48-$cmg3"
else
  export OMP_PROC_BIND=close
fi

/home/ra000003/data/chig/Benchmark_MD_Fugaku/scripts/showpwrmode.noopt
echo PJM_CUSTOM_RESOURCES=$PJM_CUSTOM_RESOURCES
echo PJM_JOBID=$PJM_JOBID
echo PJM_JOBNAME=$PJM_JOBNAME
echo PJM_STEPNUM=$PJM_STEPNUM
input=step6.6_equil
name=p2048_t12_04
mpiexec -stdout-proc ./output.${PJM_JOBID}_${PJM_STEPNUM}/%/1000r/stdout  -stderr-proc ./output.${PJM_JOBID}_${PJM_STEPNUM}/%/1000r/stderr gmx_mpi mdrun -s ${input}.tpr -g ${name}.log -nsteps 5000
#mpiexec gmx_mpi mdrun -s ${input}.tpr -g ${name}.log -nsteps 10000

