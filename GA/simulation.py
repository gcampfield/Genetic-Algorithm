from __future__ import print_function
from .population import Population

class Population_Simulation :
    def __init__(self, size, rankings, base_fitness=0, genome_size=8) :
        self.population = Population(size, rankings, base_fitness, genome_size)
        self.history = [self.population]
        self.generation = 0
        
    def run(self, duration) :
        for e in range(duration) :
            self.population.sort()
            new_population = Population(0, self.population.rankings, self.population.base_fitness, self.population.genome_size)
            for i in range(self.population.size) :
                new_population.append(self.population.reproduce())
            self.population = new_population
            self.history.append(self.population)
        self.generation += duration
            
    def print_sim(self, population=True, avgfitness=True) :
        print("Information for Generation %d:" % self.generation)
        if population :
            self.population.print_population()
        if avgfitness :
            self.population.print_average_fitness()
        
    def avg_fitness_history(self) :
        fithis = []
        for population in self.history :
            fithis.append(population.average_fitness())
        return fithis
        
    def max_fitness_history(self) :
        fithis = []
        for population in self.history :
            fithis.append(max(population.fitnesses()))
        return fithis
        
    def min_fitness_history(self) :
        fithis = []
        for population in self.history :
            fithis.append(min(population.fitnesses()))
        return fithis