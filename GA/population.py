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
        
    def print_population(self) :
        print("Population: ")
        for i in range(self.genome_size) :
            for ind in self.population :
                print(int(ind[i][0]),int(ind[i][1]), end="\t")
            print()
            
    def print_average_fitness(self) :
        print("Average Fitness: %.5f" % self.average_fitness())
        
    def print_fitnesses(population, fitness) :
        print("Fitnesses: ")
        for i in self.population :
            print(self.fitness(i),end="\t")
        print("\n")