# ESTR 2018 Group Project: Random Walk
This is our ESTR 2018 group project's code, which mainly focuses on achieving particle random movement visualization.
## Intro
Random Walk means a particle moves in a random direction along the axes 1 unit each time. We call the scenario that a particle moves on a line which is mentioned in the lecture1 as 1-dimension case. What's more, we try to consider more complex scenario and this program is attempted to show how 2-D or 3-D random walk works.

In this project, let X be a random variable which represents the distance from the original point after n steps. We have successfully calculated the laws for the discrete motion of this particle in the one-dimensional case and envisaged the possibility of a one-dimensional, continuously moving particle. Even though the lack of advanced mathematics knowledge makes the continuous 2-D random walk hard to explain generally, we still give the solution to general situation of 2-D discrete random walk.

You can find the code we used for this project in this repository, including visualizations of the discrete motion of the particle in 1, 2, and 3 dimensions, visualizations of the random directional movement of the particle in two dimensions, and fitting the results of our calculations.

## Dependency
------------------------------

1. python >= 3.7.

1. Numpy. It can be installed using pip as follows:

    `pip install numpy`
1. matplotlib. It can be installed using pip as follows:

    `pip install matplotlib`

## Quick Start
------------------------------

1. You can achieve visualisation by running the following code:

    `python {dimensional}d.py`
    
    where {dimensional} represent the dimensional you want to show.
    
1. You can achieve uniform visualisation by running the following code:

    `python uniform_2d.py`
    
1. You can achieve data Fitting by running the following code:

    `python {task}.py`
    
    where {task} represent the task you want to show.
