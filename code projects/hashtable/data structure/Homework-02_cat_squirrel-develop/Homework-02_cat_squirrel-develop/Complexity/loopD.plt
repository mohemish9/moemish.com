set title "Plot of Loop D" font ",20"
set term png
set samples 100
set style data points
set output "loopD.png"
plot "loopD.dat" using 1:2 with points title "Empirical",\
    [1:100] x**2 with lines title "Best",\
    [1:100] (x**2)*(x+1)/2 with lines title "Worst"