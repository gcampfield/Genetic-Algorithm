from __future__ import print_function
from .population import Population

class Population_Simulation :
    def __init__(self, size, rankings=False, base_fitness=400, genome_size=8, mutations=0.005) :
        '''
        size - number of members in the population
        rankings - a list of floats representing the weights of each of the genes
            -> Minimum length is 'genome_size'
        base_fitness - base number to make the drone out the importance of the fitness
        genome_size - the number of genes in the genome
        mutations - the chance of a mutation occuring, use 0 or False for no mutations
        '''
        self.population = Population(size, rankings, base_fitness, genome_size, mutations)
        self.history = [self.population]
        self.generation = 0
        
    def run(self, duration) :
        '''
        Run the simulation for 'duration' generations
        '''
        for e in range(duration) :
            self.population.sort()
            new_population = Population(0, self.population.rankings, self.population.base_fitness, self.population.genome_size, self.population.mutations)
            for i in range(self.population.size) :
                new_population.append(self.population.reproduce())
            self.population = new_population
            self.history.append(self.population)
        self.generation += duration
            
    def print_sim(self, population=True, avgfitness=True) :
        '''
        Print the current state of the simulation.

        population - whether to print the population or not
        avgfitness - whether to print the average fitness or not
        '''
        print("Information for Generation %d:" % self.generation)
        if population :
            self.population.print_population()
        if avgfitness :
            self.population.print_average_fitness()
        
    def avg_fitness_history(self) :
        '''
        Get a list of all of the average fitnesses for the population over time

        returns: a list of all of the average fitnesses for each generation
        '''
        fithis = []
        for population in self.history :
            fithis.append(population.average_fitness())
        return fithis
        
    def max_fitness_history(self) :
        '''
        Get a list of all of the maximum fitnesses for the population over time

        returns: a list of all of the maximum fitnesses for each generation
        '''
        fithis = []
        for population in self.history :
            fithis.append(max(population.fitnesses()))
        return fithis
        
    def min_fitness_history(self) :
        '''
        Get a list of all of the minimum fitnesses for the population over time

        returns: a list of all of the minimum fitnesses for each generation
        '''
        fithis = []
        for population in self.history :
            fithis.append(min(population.fitnesses()))
        return fithis
