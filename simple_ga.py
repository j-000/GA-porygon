import random
import string
from datetime import datetime
from matplotlib import pyplot
import string

WHITESPACE = ' '
GENES_SET = string.ascii_lowercase + WHITESPACE

target = 'porygon pikachu mama mia'
pop_max = 1000
initial_pop = [''.join(random.choices(GENES_SET, k=len(target))) for _ in range(pop_max)]
mutation_rate = 0.01

# Charts data
x_data, y_data = [], []


def fitness(member):
    score = 0
    for (a, b) in zip(member, target):
        if a == b:
            score += 1
    return score / len(target)


def find_fittest():
    scores = [(i, fitness(i)) for i in initial_pop]
    maxp = max(scores, key=lambda x: x[1])
    return maxp


def create_mating_pool():
    pool = []
    for m in initial_pop:
        freq = int(fitness(m) * 10)
        pool += [m for _ in range(freq)]
    return pool


def crossover(a, b):
    midpoint = random.randint(0, len(target) + 1)
    return a[:midpoint] + b[midpoint:]


found = False
generation = 0
MAX_ITER = 1000
while not found:
    generation += 1

    # Find fittest
    fittest, score = find_fittest()
    print(generation, fittest, score)

    # charts
    x_data.append(datetime.now())
    y_data.append(score)

    # Evaluate
    if fittest == target:
        print(f'Result in {generation} generations: ', fittest)
        break

    # Mating pool
    mating_pool = create_mating_pool()

    temp_pop = []
    for i in initial_pop:
        # Pick 2 parents
        parent_a = random.choice(mating_pool)
        parent_b = random.choice(mating_pool)
        child = crossover(parent_a, parent_b)
        temp_pop.append(child)

    # Replace pop
    initial_pop = temp_pop

    if generation == MAX_ITER:
        print('Nothing found in 5000 generations. Adjust the parameters.')
        break


figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')
pyplot.show()
