#!/usr/bin/python

from __future__ import print_function
from random import random

class Population :    
    def __init__(self, size, rankings, base_fitness=40, genome_size=8) :
        self.size = size
        self.population = []
        self.rankings = rankings
        self.base_fitness = base_fitness
        self.genome_size = genome_size
        for _ in range(size) :
            self.makePerson()
        
    def makePerson(self) :
        p = []
        for _ in range(self.genome_size) :
            p.append([int(round(random())), int(round(random()))])
        self.population.append(p)
        
    def fitness(self, ind) :
        fit = self.base_fitness
        for i in range(self.genome_size) :
            fit += (ind[i][0] or ind[i][1])*self.rankings[i]*10
        return fit
        
    def sort(self) :
        self.population.sort(key=self.fitness)
        
    def select(self) :
        fitnesses = [self.fitness(i) for i in self.population]
        total = sum(fitnesses)+0.0
        fitnesses[0] = fitnesses[0]/total
        for i in range(1, self.size) :
            fitnesses[i] = fitnesses[i]/total+fitnesses[i-1]
        rand = random()
        for i in range(self.size) :
            if rand < fitnesses[i] :
                return self.population[i]
            
    def reproduce(self) :
        def crossover(x) :
            point = int(random()*self.genome_size) + 1
            new_x = list(x)
            for i in range(point, self.genome_size) :
                new_x[i].reverse()
            return new_x
        
        def mutate(x) :
            for i in range(self.genome_size) :
                for a in range(len(x[0])) :
                    if random() < .05 :
                        x[i][a] = abs(x[i][a] - 1)
        
        x, y = self.select(), self.select()
        
        new_x, new_y = crossover(x), crossover(y)
        strand_x = int(round(random()))
        strand_y = int(round(random()))
        child = [[x[i][strand_x], y[i][strand_y]] for i in range(len(x))]
        
        mutate(child)
        
        return child
    
    def append(self, child) :
        self.population.append(child)
        self.size += 1
        
    def average_fitness(self) :
        total = 0.0
        for i in self.population :
            total += self.fitness(i)
        return total / self.size
        
    def print(self) :
        print("Population: ")
        for i in range(self.genome_size) :
            for ind in self.population :
                print(int(ind[i][0]),int(ind[i][1]), end="\t")
            print()
            
    def print_fitnesses(population, fitness) :
        print("Fitnesses: ")
        for i in self.population :
            print(self.fitness(i),end="\t")
        print("\n")

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
            
    def print(self, population=True, avgfitness=True) :
        print("Information for Generation %d:" % self.generation)
        if population :
            self.population.print()
        if avgfitness :
            print("Average Fitness: ", self.population.average_fitness())
        
    def fitness_history(self) :
        fithis = []
        for population in history :
            avgfitness = population.average_fitness()
            fithis.append((avgfitness-avgfitness%.001))
        return fithis

FITNESS_RANKINGS = [0.65, 0.31, 0.38, 0.83, 0.58, 0.05, 0.51, 0.81, 0.04, 0.37]
simulation = Population_Simulation(500, FITNESS_RANKINGS)

simulation.print(population=False)

print("\nRunning Simulation for 100 generations...\n")
simulation.run(100)

simulation.print(population=False)