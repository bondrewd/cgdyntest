#!/bin/bash

j=01

for n in {01,02,03,04,05}; do
    cp p128_t12_XX.sh p128_t12_${n}.sh
    sed -e "s/XX/$n/g" -i p128_t12_${n}.sh
    sleep 0.1
    pjsub p128_t12_${n}.sh
done

