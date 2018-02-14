#!/bin/bash

gnuplot -p -e "pl 'part5.dat' u 1:2 t 'Electron 1', 'part5.dat' u 9:10 t 'Electron 2', 'part5.dat' u 17:18 t 'Electron 3', 'part5.dat' u 25:26 t 'Electron 4', 'part5.dat' u 33:34 t 'Proton 1', 'part5.dat' u 41:42 t 'Proton 2', 'part5.dat' u 49:50 t 'Proton 3', 'part5.dat' u 57:58 t 'Proton 4' ; set xlabel \"x coordinate [m]\" ; set ylabel \"y coordinate [m]\" ; set xr [-1.1:1.1] ; set yr [-1.1:1.1] ; set key center ; rep"


