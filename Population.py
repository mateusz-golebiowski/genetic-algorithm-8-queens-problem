import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import TextBox

import Chromosome

class Population:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.selected = []
        self.generation = 0
        self.initialPopulation = self

    def fitness(self):
        print("Fitness computing...")
        for ch in self.chromosomes:
            ch.computeFitness()
    def selection(self):
        print("Generation: {}".format(self.generation+1))
        self.selected = []
        for g in range(0,3):
            m = max([ i.fitness for i in self.chromosomes])
            added = False
            for ch in self.chromosomes:
                if ch.fitness == m and added == False: 
                    self.selected.append(ch)
                    self.chromosomes.remove(ch)
                    added = True
        print("Selected chromosomes")
        show =[i.genes for i in self.selected]
        print(show)
                    
    def crossover(self):
        print("Crossover...")
        self.chromosomes = [
            Chromosome.Chromosome(self.selected[0].genes[:4]+self.selected[1].genes[4:]),
            Chromosome.Chromosome(self.selected[1].genes[:4]+self.selected[0].genes[4:]),
            Chromosome.Chromosome(self.selected[0].genes[:4]+self.selected[2].genes[4:]),
            Chromosome.Chromosome(self.selected[2].genes[:4]+self.selected[0].genes[4:]),

        ]
        print("Population after crossover: ")
        
        print([i.genes for i in self.chromosomes])

        self.generation +=1
    def mutation(self):
        print("Mutation...")

        print("Population after mutation")
        print([i.genes for i in self.chromosomes])

    def genReport(self, genes):
        x = [1.5 ,2.5, 3.5, 4.5, 5.5, 6.5, 7.5 ,8.5]
        y =[ g+0.5 for g in genes ]

        return [x, y]
    def showResult(self):

        fig = plt.figure(figsize=(12, 8))


        data = self.genReport(self.chromosomes[0].genes)
       
        sub1 = plt.subplot(2, 2, 1)
     
        sub1.plot(data[0], data[1], "ro")
        sub1.axis([1, 9, 1, 9])
        sub1.grid(True)
        plt.setp(sub1.get_xticklabels(), visible=False)
        plt.setp(sub1.get_yticklabels(), visible=False)
        sub1.tick_params(axis='both', which='both', length=0)

        data = self.genReport(self.chromosomes[1].genes)
       
        sub2 = plt.subplot(2, 2, 2)
     
        sub2.plot(data[0], data[1], "ro")
        sub2.axis([1, 9, 1, 9])
        sub2.grid(True)
        plt.setp(sub2.get_xticklabels(), visible=False)
        plt.setp(sub2.get_yticklabels(), visible=False)
        sub2.tick_params(axis='both', which='both', length=0)

    
        

        data = self.genReport(self.chromosomes[2].genes)
       
        sub3 = plt.subplot(2, 2, 3)
     
        sub3.plot(data[0], data[1], "ro")
        sub3.axis([1, 9, 1, 9])
        sub3.grid(True)
        plt.setp(sub3.get_xticklabels(), visible=False)
        plt.setp(sub3.get_yticklabels(), visible=False)
        sub3.tick_params(axis='both', which='both', length=0)


        data = self.genReport(self.chromosomes[3].genes)
       
        sub4 = plt.subplot(2, 2, 4)
     
        sub4.plot(data[0], data[1], "ro")
        sub4.axis([1, 9, 1, 9])
        sub4.grid(True)
        plt.setp(sub4.get_xticklabels(), visible=False)
        plt.setp(sub4.get_yticklabels(), visible=False)
        sub4.tick_params(axis='both', which='both', length=0)

        axbox = plt.axes([0.1, 0.01, 0.4, 0.05])
        text_box = TextBox(axbox, 'Generation', initial="10")
        #text_box.on_submit(submit)

        axbutton = plt.axes([0.81, 0.01, 0.04, 0.05])
        button = Button(axbutton, 'ok')
        #button.on_clicked(fu)

        axCheck = plt.axes([0.7, -0.03, 0.07, 0.15], zorder=-1, frameon=False)
        check = CheckButtons(axCheck, ["Mutation"], [0])
        plt.show()

            