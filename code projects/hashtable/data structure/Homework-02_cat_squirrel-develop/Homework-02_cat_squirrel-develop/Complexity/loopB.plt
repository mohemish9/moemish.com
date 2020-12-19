set title "Plot of Loop B" font ",20"
set term png
set samples 100
set style data points
set output "loopB.png"
plot "loopB.dat" using 1:2 with points title "Empirical",\
    [1:100] x*(x+1)/2 with lines title "output"