#!/bin/bash

gnuplot -p -e "pl 'part2.dat' u 0:2 t 'Proton', 'part2.dat' u 0:10 t 'Electron' ; set xlabel \"Time [ms]\" ; set ylabel \"Distance [m]\" ; set key top right ; rep"


