set title "Plot of Loop E" font ",20"
set term png
set samples 100
set style data points
set output "loopE.png"
plot "loopE.dat" using 1:2 with points title "Empirical",\
    [1:100] (x**2)/3 with lines title "output"