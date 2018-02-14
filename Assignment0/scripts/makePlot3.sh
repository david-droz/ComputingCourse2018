#!/bin/bash

gnuplot -p -e "pl 'part3.dat' u 1:2 t 'Proton', 'part3.dat' u 9:10 t 'Electron' ; set xlabel \"x coordinate [m]\" ; set ylabel \"y coordinate [m]\" ; set xr [-1.1:1.1] ; set yr [-1.1:1.1] ; set key top left ; rep"



