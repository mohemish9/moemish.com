set title "Plot of Loop A" font ",20"
set term png
set samples 100
set style data points
set output "loopA.png"
plot "loopA.dat" using 1:2 with points title "Empirical",\
    [1:100] x with lines title "Expected"
