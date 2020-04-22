import random
import re

# Starting with a minimalistic set of genes
# to avoid complexity nightmares.
REGEX_SET = ('\d','\w', '+', '*', '\s')

# Again, minimalistic approach and then scale up.
target = 'mat12'

pop_max = 100
initial_pop = [''.join(random.choices(REGEX_SET, k=len(target))) for _ in range(pop_max)]
mutation_rate = 0.0

# Charts data
x_data, y_data = [], []


def regex_fitness(member):
    """
    This function is trouble...
    """
    score = 0
    try:
        member_regex = re.compile(member)
        match = member_regex.match(target)
        if match:
            return match
    except Exception:
        pass
    return score


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

    # Testing area
    for i in initial_pop:
        print(i, regex_fitness(i))
    break

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


# figure = pyplot.figure()
# line, = pyplot.plot_date(x_data, y_data, '-')
# pyplot.show()
