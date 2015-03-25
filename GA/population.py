from __future__ import print_function
from random import random

class Population :    
    def __init__(self, size, rankings=False, base_fitness=400, genome_size=8, mutations=.05) :
        '''
        size - number of members in the population
        rankings - a list of numbers representing the weights of each of the genes
            -> Minimum length is 'genome_size'
        base_fitness - base number to make the drone out the importance of the fitness
        genome_size - the number of genes in the genome
        mutations - the chance of a mutation occuring, use 0 or False for no mutations
        '''
        self.size = size
        self.population = []
        if rankings :
            self.rankings = rankings
        else :
            self.rankings = [50 for _ in range(genome_size)]
        self.base_fitness = base_fitness
        self.genome_size = genome_size
        self.mutations = mutations
        for _ in range(size) :
            self.makePerson()
        
    def makePerson(self) :
        '''
        Add a random genotyped person to the population
        '''
        p = []
        for _ in range(self.genome_size) :
            p.append([round(random()), round(random())])
            # p.append([(1.0 if random() < .25 else 0.0), (1.0 if random() < .25 else 0.0)])
            # p.append([0.0, 0.0])
        self.population.append(p)
        
    def fitness(self, ind) :
        '''
        ind - An individual's genome

        returns: fitness of the individual
        '''
        fit = self.base_fitness
        for i in range(self.genome_size) :
            fit += (ind[i][0] or ind[i][1])*self.rankings[i]
        return fit
        
    def sort(self) :
        '''
        Sort the population of individuals based on their fitness from low to high
        '''
        self.population.sort(key=self.fitness)
        
    def select(self) :
        '''
        Select a random individual from the population by a roulette-wheel selection method

        returns: selected individual
        '''
        fitnesses = self.fitnesses()
        total = sum(fitnesses)+0.0
        if total==0.0 : return self.population[0]
        fitnesses[0] = fitnesses[0]/total
        for i in range(1, self.size) :
            fitnesses[i] = fitnesses[i]/total+fitnesses[i-1]
        rand = random()
        for i in range(self.size) :
            if rand < fitnesses[i] :
                return self.population[i]
    
    def mutate(self, x) :
        '''
        Muatate an individual randomly with a mutation chance of self.mutations
        '''
        for i in range(self.genome_size) :
            for a in range(len(x[0])) :
                if random() < self.mutations :
                    x[i][a] = abs(x[i][a] - 1)
                    
    def crossover(self, x) :
        '''
        Crossover the two strands of an individual without harming the original

        returns: new chromosome after crossing over
        '''
        point = int(random()*self.genome_size) + 1
        new_x = [i[:] for i in x]
        for i in range(point, self.genome_size) :
            new_x[i].reverse()
        return new_x
                    
    def reproduce(self) :
        '''
        From the population, randomly select two parents (based on their fitness)
        and produce a child randomly from their genomes and mutate it

        returns: child produced
        '''
        x, y = self.select(), self.select()
        
        new_x, new_y = self.crossover(x), self.crossover(y)
        strand_x = int(round(random()))
        strand_y = int(round(random()))
        child = [[x[i][strand_x], y[i][strand_y]] for i in range(len(x))]
        
        if self.mutations :
            self.mutate(child)
        
        return child
    
    def append(self, child) :
        '''
        Append a specified individual to a population and increase the size of the population

        child - the genome of the individual to be added
        '''
        self.population.append(child)
        self.size += 1
        
    def fitnesses(self) :
        '''
        Calculate the fitnesses of the population

        returns: a list of all of fitnesses for each individual in the population
        '''
        fits = []
        for i in self.population :
            fits.append(self.fitness(i))
        return fits
        
    def average_fitness(self) :
        '''
        Calculate the average fitness of the population

        returns: average fitness for the population
        '''
        return sum(self.fitnesses()) / self.size
        
    def print_population(self) :
        '''
        Print the population in a readable manner
        '''
        print("Population: ")
        for i in range(self.genome_size) :
            for ind in self.population :
                print(int(ind[i][0]),int(ind[i][1]), end="\t")
            print()
            
    def print_average_fitness(self) :
        '''
        Print the average fitness of the population
        '''
        print("Average Fitness: %.5f" % self.average_fitness())
        
    def print_fitnesses(self) :
        '''
        Print all of the fitnesses for each individual in the population
        '''
        print("Fitnesses: ")
        for i in self.population :
            print(self.fitness(i),end="\t")
        print("\n")