#!/bin/bash

j=01

for n in {01,02,03,04,05}; do
    cp p4096_t12_XX.sh p4096_t12_${n}.sh
    sed -e "s/XX/$n/g" -i p4096_t12_${n}.sh
    sleep 0.1
    pjsub p4096_t12_${n}.sh
done

