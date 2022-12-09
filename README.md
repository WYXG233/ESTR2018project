# ESTR 2018 Group Project: Random Walk
This is our ESTR 2018 group project's code, which mainly focuses on achieving particle random movement visualization.
## Intro
Random Walk, means a particle moves randomly each time. So, when a particle moves on a line as the professor mentioned in the first lecture, it’s a 1-dimension case. If we expand the question. When it comes to 2 or 3 dimensions, which means the particle can move in more directions, this question will be more interesting and complex.

In this project, let X be a random variable which represents the distance from the original point after n steps. We have successfully calculated the laws for the discrete motion of this particle in the one-dimensional case and envisaged the possibility of a one-dimensional, continuously moving particle. This is even though we lack sufficient mathematical knowledge to complete the subsequent derivation. In the two-dimensional case, we give a formula for the discrete motion.

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
