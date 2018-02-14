#!/bin/bash

gnuplot -p -e "pl 'part4.dat' u 1:2 t 'Proton', 'part4.dat' u 9:10 t 'Electron 1', 'part4.dat' u 17:18 t 'Electron 2' ; set xlabel \"x coordinate [m]\" ; set ylabel \"y coordinate [m]\" ; set key top center ; rep"


