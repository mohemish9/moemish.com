set title "Plot of Loop Sample" font ",20"
set term png
set samples 100
set style data points
set output "sample.png"
plot "sample.dat" using 1:2 with points title "Empirical",\
    [1:100] .5*x with lines title "Best",\
    [1:100] 2*x with lines title "Worst"


