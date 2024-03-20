# evolutionary-algorithm-toolkit

This repository contains a collection of optimization algorithms implemented in Python. Currently, it includes implementations of vector gradient descents and a genetic algorithm.

# Setup

Open your terminal and install the following packages and libraries:

    sudo apt install python3
    sudo apt install python3-pip
    sudo pip install numpy
    sudo pip install matplotlib

# Task 3 - Particle Swarm Optimization with calculated  t_k

For task you need fork my repository to make changes in python script. You can learn abaout working with forks in [Github Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo "Github Fork").

Once forked, a new repository would appear in your repository section based on my code. Here you can create commits, files, etc., without needing my permissions.

## Note

You don’t need to follow the following sections for the task. Only if you would like to learn how to connect my repository (javi-hv) with your repository (e.g., fabian-repository), you can follow the following section:

Firstly you can review the direction or url of origin 

    git remote -v

Now you can update the new remote direction, type and replace <new_url> with your ssh difrection of forked repository in your repositories section (No copy the original repository in javi-hv profile ):

    git remote add upstream <new_url> # upstream can be any other words  but I recommend you upstream! 
    git pull upstream main 

now we can do changes and then

    git push origin main