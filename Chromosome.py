
class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0

    def computeFitness(self):
        good = 0
        wrong = 0
        arr = [True, True, True, True, True, True, True, True ]
        for ii, j in enumerate(self.genes):
            for mm, n in enumerate(self.genes):
                i = ii+1
                m = mm+1
                if (ii != mm):
                    if (j == n):
                        arr[mm] = False
                    if (j == n + (mm-ii)):
                        arr[mm] = False
                    if (j == n - (mm-ii)):
                        arr[mm] = False
        
        for val in arr:
            if (val):
                good += 1
            else:
                wrong += 1
             
        self.fitness = good - wrong
