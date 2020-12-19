set title "Plot of Loop C" font ",20"
set term png
set samples 100
set style data points
set output "loopC.png"
plot "loopC.dat" using 1:2 with points title "Empirical",\
    [1:100] x**2 * ( x**3 - x - 1 ) * log(2*x)/log(2) with lines title "Output"