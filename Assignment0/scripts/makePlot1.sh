#!/bin/bash

gnuplot -p -e "pl 'part1.dat' u 0:2 t 'Electron 1 position', 'part1.dat' u 0:10 t 'Electron 2 position', 'part1.dat' u 0:5 t 'Electron 1 speed', 'part1.dat' u 0:13 t 'Electron 2 speed' ; set xlabel \"Time [ms]\" ; set ylabel \"Distance from origin [m] or speed [m/s]\" ; set key top left ; rep"


