#!/usr/bin/python

from __future__ import print_function
from GA.simulation import Population_Simulation
import matplotlib.pyplot as plt

FITNESS_RANKINGS = [0.65, 0.31, 0.38, 0.83, 0.58, 0.05, 0.51, 0.81, 0.04, 0.37]
simulation = Population_Simulation(10, FITNESS_RANKINGS)

simulation.print_sim(population=True)

print("\nRunning Simulation for 100 generations...\n")
simulation.run(100)

simulation.print_sim(population=True)

plt.plot(simulation.max_fitness_history(), 'g')
plt.plot(simulation.avg_fitness_history(), 'b')
plt.plot(simulation.min_fitness_history(), 'r')
plt.show()