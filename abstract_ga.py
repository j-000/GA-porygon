import random
import statistics


class AbstractGA:

    def __init__(self, target, pop_max, mutation_rate,
                 genes_set, fitness_function, crossover_function,
                 max_iter=1000, charter=None, info=True):
        self.target = target
        self.pop_max = pop_max
        self.mutation_rate = mutation_rate
        self.max_iter = max_iter
        self.charter = charter
        self.info = info
        self.genes_set = genes_set
        self.generation = 0
        self.initial_pop = [''.join(random.choices(self.genes_set, k=len(target))) for _ in range(pop_max)]
        # fitness_function and crossover_function are abstracted
        self.fitness_function = fitness_function
        self.crossover_function = crossover_function

    def find_fittest(self):
        """
        Apply fitness function to each member of the population and
        return a tuple (member, score)
        """
        scores = [(member, self.fitness_function(member)) for member in self.initial_pop]
        member, score = max(scores, key=lambda x: x[1])
        return member, score

    def create_mating_pool(self):
        """
        Return a list of members with frequency relative to their
        fitness score, distributed between 1 and 10. The higher the score
        the more times the member is present on the mating pool and the higher the
        chances of mating.
        """
        pool = []
        for member in self.initial_pop:
            freq = int(self.fitness_function(member) * 10)
            pool += [member for _ in range(freq)]
        return pool

    def mutate_genes(self, element):
        """
        Return the genes of an element possibly mutated.
        The mutation takes into account the mutation_rate
        and the genes_set.
        """
        temp = []
        for i, e in enumerate(element):
            if random.random() < self.mutation_rate:
                e = random.choice(self.genes_set)
            temp.append(e)
        return ''.join(temp)

    def run(self):
        while True:
            self.generation += 1

            # Find fittest
            fittest, score = self.find_fittest()

            if self.info:
                print(f'\nGeneration: {self.generation}')
                print(f'Fittest:    {fittest}')
                print(f'Score:      {score}')

            # charts
            if self.charter:
                # Labels
                self.charter.x_data.append(self.generation)
                # Generation Fittest score
                self.charter.y_fittest.append(score)
                # Generation Mean score
                scores = [self.fitness_function(member) for member in self.initial_pop]
                scores_mean = round(sum(scores) / len(scores), 3)
                self.charter.y_mean.append(scores_mean)
                # Generation Standard deviation score
                scores_std_dev = round(statistics.stdev(scores), 3)
                self.charter.y_std_dev.append(scores_std_dev)

            # Evaluate
            if fittest == self.target:
                if self.info:
                    print(f'Result in {self.generation} generations: ', fittest)
                break

            # Mating pool
            mating_pool = self.create_mating_pool()

            temp_pop = []
            for _ in self.initial_pop:
                # Pick 2 parents
                parent_a = random.choice(mating_pool)
                parent_b = random.choice(mating_pool)
                child = self.crossover_function(parent_a, parent_b)
                child = self.mutate_genes(child)
                temp_pop.append(child)

            # Replace pop
            self.initial_pop = temp_pop

            if self.generation == self.max_iter:
                if self.info:
                    print(f'Nothing found in {self.max_iter} generations. Adjust the parameters.')
                break

    def display_charts(self):
        self.charter.main()
