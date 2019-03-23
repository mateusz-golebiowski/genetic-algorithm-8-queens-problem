
class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0
    
    def suma(self, x):
        s = 0
        i = 1
        while i<x:
            s+=i
            i+=1
        return s

    def computeFitness(self):
        good = 0
        wrong = 0
        x = self.genes.count(1)
        if x == 1: good += 1
        if x > 1: wrong += self.suma(x)
        
        x = self.genes.count(2)
        if x == 1: good += 1
        if x > 1: wrong +=  self.suma(x)
        
        x = self.genes.count(3)
        if x == 1: good += 1
        if x > 1: wrong +=  self.suma(x)

        x = self.genes.count(4)
        if x == 1: good += 1
        if x > 1: wrong +=  self.suma(x)
        
        x = self.genes.count(5)
        if x == 1: good += 1
        if x > 1: wrong += self.suma(x)
        
        x = self.genes.count(6)
        if x == 1: good += 1
        if x > 1: wrong += self.suma(x)
        
        x = self.genes.count(7)
        if x == 1: good += 1
        if x > 1: wrong +=  self.suma(x)

        x = self.genes.count(8)
        if x == 1: good += 1
        if x > 1: wrong += self.suma(x)
             
        self.fitness = good - wrong
        print("For Chromosome: {}".format(self.genes))
        print("Good: {}".format(good))
        print("Wrong: {}".format(wrong))
        print("Fitness: {}".format(self.fitness))