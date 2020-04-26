import random
import string
from abstract_ga import AbstractGA


class BasicSimulation(AbstractGA):

    def __init__(self, target, pop_max, mutation_rate, max_iter=1000, charter=None, info=True):
        super().__init__(target, pop_max, mutation_rate, genes_set=string.ascii_letters + ' ',
                         fitness_function=self.fitness, crossover_function=self.crossover, max_iter=max_iter,
                         charter=charter, info=info)

    def fitness(self, member):
        score = 0
        for (a, b) in zip(member, self.target):
            if a == b:
                score += 1
        return round(score / len(self.target), 3)

    def crossover(self, a, b):
        midpoint = random.randint(0, len(self.target) + 1)
        return a[:midpoint] + b[midpoint:]
