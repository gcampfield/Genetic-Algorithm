#!/usr/bin/python

from __future__ import print_function
from GA.simulation import Population_Simulation
import matplotlib.pyplot as plt

# Initialize the Population_Simulation
FITNESS_RANKINGS = [65, 31, 38, 83, 58, 05, 51, 81, 04, 37]
simulation = Population_Simulation(20, FITNESS_RANKINGS, base_fitness=0, genome_size=10, mutations=False)

# Print initial state of the simulation
simulation.print_sim(population=False)

print("\nRunning Simulation for 100 generations...\n")
simulation.run(100)

# Print final state of the simulation
simulation.print_sim(population=False)

# Graph the simulation with matplotlib
plt.plot(simulation.max_fitness_history(), 'g', label="Max. Fitness")
plt.plot(simulation.avg_fitness_history(), 'b', label="Average Fitness")
plt.plot(simulation.min_fitness_history(), 'r', label="Min. Fitness")
plt.legend(loc="lower right")
plt.show()