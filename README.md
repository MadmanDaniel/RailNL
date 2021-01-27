# RailNL

## Purpose
The case of this project is to create a heuristic within Python that generates a lining system for intercity trains with the aim of optimizing the overall quality of the lines. This can be done by maximizing the goal function given in the exercise. The objective function can be described as follows: K = p * 10000 - (T * 100 + Min), where K is the quality of the train control system, p is a fraction of the number of connections used, T the number of paths used, and Min is the total time in minutes of all used paths. There are two conditions that must be met when creating a train line system. The first is that a route has a maximum time length, and the second condition is that a train line system has a maximum number of paths. 

## Requirements
To use this code, prior packages are required to make this code work. These can be installed through the command:
<pre> pip install -r requirements.txt </pre>

## How does it work?
Use the following statement to run the code: <pre> python main.py </pre> The program will first ask you which part of the Netherlands you want to use. The program will then ask you which algorithm you want to use. There are three options: Random, Greedy and Hill Climber. Each algorithm produces an image of the chosen paths and the score

<img src = "https://github.com/MadmanDaniel/RailNL/blob/main/doc/command.png">

## Extensions
- networkx
- matplotlib
- random
- csv
- pandas

## Structure 

The following list describes the most important folders and files in the project, and where to find them:

- **/code**: All code for this project
  - **/code/algorithm**: The code for the algorithms
  - **/code/classes**: The classes for this case
  - **/code/visualisation**: The code for the visualizations
- **/data**: The data files needed to visualize the graph

## Authors
Team name: **Team Rocket**
* Daniel Djuly
* Hatim Hashi
* Elvin Li
