<!--- Note: This is how you add a comment in Markdown! --->

# Sample

<!--- If you're curious, the LaTeX for this summation is: \sum_{i=1}^N 2 ---> 
* **Best Case Summation**: ![Sum as i goes from 1 to N of 2](https://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D1%7D%5EN%202)

* **Best Case Closed Form**: `0.5N` 

<!--- the LaTeX for this summation : \sum_{i=1}^N 2 ---> 
* **Worst Case Summation**: ![Sum as i goes from 1 to N of 2](https://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D1%7D%5EN%202)

* **Worst Case Closed Form**: `2N`

* **Plot**: ![A sample plot image](https://www.cs.hmc.edu/cs70/assets/HW2_sample_plot.png)
* **Observations**: Although we calculated a separate *best* and *worst* case line to plot here, our empirical observations were always right in the middle. 


# Loop A

* **Summation**: ![Sum as i goes from 0 to N-1 of 1]
* **Closed Form**: `N`
(https://latex.codecogs.com/gif.latex?\sum_{i=0}^{N-1}1)
* **Plot**: ![loopa](https://user-images.githubusercontent.com/43027778/45794726-e0366e00-bc4c-11e8-8540-a8609825cc7d.png)
* **Observations**: In this case, the plot and the empirical graphs lined up and both are linear functionss. Since the summation was of a constant, there is a direct correlation between the number of times the loop runs and the value of total.

# Loop B

* **Summation**: ![Sum as i goes from 0 to N-1 of sum as j goes from 1 to N-1 of 1]
* **Closed Form**:`N(N+1)/2`
(https://latex.codecogs.com/gif.latex?\sum_{i=0}^{N-1}\sum_{j=1}^{N-1}1)
* **Plot**: ![loopb](https://user-images.githubusercontent.com/43027778/45794714-ce54cb00-bc4c-11e8-94ea-253fb3d1ecf6.png)
* **Observations**: In this function, there is no worst or best case scenarios, thus the reasn why thh empirical and the output plots match perfectly. 


# Loop C

* **Summation**: ![Sum as i' goes from 0 to ((N^2)-1)/2 of the sum as j goes from 0 to log2(N) of the sum as k goes from 0 to (2*N*i')-1 of 1 ]
* **Closed Form**: `(N^2*(N^3 - N - 1)*log(2N))/log(2)`
(https://latex.codecogs.com/gif.latex?\sum_{i`=0}^{(N^2&space;-1)/2}\sum_{j=0}^{log(N)/log(2)}\sum_{k=0}^{(2*N*i`)-1}1)
* **Plot**: ![loopc](https://user-images.githubusercontent.com/43027778/45795029-60110800-bc4e-11e8-9fd6-68f5ab06c381.png)

* **Observations**: In this case, there was no best or worst case scenarios thus, in theory, the grpahs should line up. However, in this case, the empirical value goes over the limit of an unsigned int type, resulting in over writing bits and reverting to a smaller number within the capacity of an unsigned int.


# Loop D

* **Best Case Summation**: ![sum as i goes from 0 to N-1 of N]
* **Best Case Closed Form**: `N^2`
(https://latex.codecogs.com/gif.latex?\sum_{i=0}^{N-1}N)
* **Worst Case Summation**: ![sum as i goes from 0 to N-1 of N(N+1)/2]
* **Worst Case Closed Form**:`N^2(N+1)/2`
(https://latex.codecogs.com/gif.latex?\sum_{i=0}^{N-1}(N(N&plus;1))/2)
* **Plot**: ![loopd](https://user-images.githubusercontent.com/43027778/45794539-17584f80-bc4c-11e8-9a8c-7b568c790001.png)
* **Observations**: In this graph,there is a best-case and worst-case scenarios plotted on the graph. The empirical values of the plot are always within the limit of the worst-case and best-case plots, showing that the empirical data is within those limits.  


# Loop E

* **Summation**: ![sum as i goes from 1 to N/3 of the sum as j goes from 0 to N of 1]
* **Closed Form**: `N^2/3`
(https://latex.codecogs.com/gif.latex?\sum_{i=1}^{N/3}\sum_{j=0}^{N-1}1)
* **plot** ![loope](https://user-images.githubusercontent.com/43027778/45796829-6788df00-bc57-11e8-8ab0-8ea7a75c025e.png)
* **Observations**:This function has no best or worst case scenarios. The function lines up with teh empirical dat since there are always a set number of time the lops will run that will not change.
