import Chromosome
import Population
import random


p = Population.Population([
    Chromosome.Chromosome([random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),
    random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8)]),
    Chromosome.Chromosome([random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),
    random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8)]),
    Chromosome.Chromosome([random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),
    random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8)]),
    Chromosome.Chromosome([random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),
    random.randint(1, 8),random.randint(1, 8),random.randint(1, 8),random.randint(1, 8)]),
])

p.run()





