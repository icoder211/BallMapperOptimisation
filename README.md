# Ball Mapper Optimisation

This repository contains an optimised version of the Ball Mapper Algorithm
The standard CRAN implementation can be found here: [CRAN implementation of Ball Mapper](https://cran.r-project.org/web/packages/BallMapper/index.html). The relevant files are also included in this repp in `R` folder for easy reference. 

In this repo, the `ball.cpp` file contains the optimsed code
The optimisations are:
- The quadratic procedure of finding and removing duplicate edges has been optimised to $O(nlogn)$. This refers to [this block](https://github.com/icoder211/BallMapperOptimisation/blob/main/R/BallMapper.R#L129-L162)
- The code has been deployed in C++, speeding up the runtime by **100 times**

## Results
The Boston property dataset (/R/data) was modified to create datasets of different sizes and here are the runtimes of the CRAN implementation and our C++ code:
![Optimised algo performance](ballmapperopt.png)
As can be seen, there is a consistent 100x improvement in runtime.