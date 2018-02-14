#!/bin/bash

gnuplot -p -e "pl 'part6.dat' u 1:2 t 'Electron', 'part6.dat' u 9:10 t 'Proton 1', 'part6.dat' u 17:18 t 'Proton 2', 'part6.dat' u 25:26 t 'Proton 3', 'part6.dat' u 33:34 t 'Proton 4' ; set xlabel \"x coordinate [m]\" ; set ylabel \"y coordinate [m]\" ; set key top center ; rep"


