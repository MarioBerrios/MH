#!/bin/bash

cat << _end_ | gnuplot
set terminal epslatex
set output "path/to/file.tex"

#Label and data format
#set format y "%.2f" 
#set decimalsign '.'
#set format x "%.1f" 
#set decimalsign '.'

#Border frame format
set border 3
set xtics nomirror
set ytics nomirror
#set xtics 1, 5, 50

#grid style
set style line 12 lc rgb '#808080' lt 0 lw 0.5
set grid back ls 12

#Label text
set xlabel "Ciudades"
set ylabel "Porcentaje (%)"

#Legend style
set key center top width 0 height 1 box lt -1 lw 1
#set nokey

#Line style
#set style line 101 lw 1.5 lt rgb "#994455"
#set style line 102 lw 1.5 lt rgb "#997700"
#set style line 103 lw 1.5 lt rgb "#004488"

plot 'path/to/file.txt' using 1:2 t "Title 1" w l, \
'path/to/file.txt' using 1:3 t "Title 2" w l
_end_
