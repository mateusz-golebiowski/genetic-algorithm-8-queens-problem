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

        self.showResult()
        
        


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


    def run(self,data):
        self.fitness()

        print([i.genes for i in self.chromosomes])
        while self.generation < 100:
            self.selection()
            self.crossover()
            self.mutation()
            self.fitness()
        data = self.genReport(self.chromosomes[0].genes)
        self.line1.set_ydata(data[1])

        data = self.genReport(self.chromosomes[1].genes)
        self.line2.set_ydata(data[1])

        data = self.genReport(self.chromosomes[2].genes)
        self.line3.set_ydata(data[1])

        data = self.genReport(self.chromosomes[3].genes)
        self.line4.set_ydata(data[1])

    def showResult(self):
        self.fig = plt.figure(figsize=(10, 6))


        data = self.genReport(self.chromosomes[0].genes)
       
        self.sub1 = plt.subplot(2, 2, 1)
     
        self.line1, = self.sub1.plot(data[0], data[1], "ro")
        self.sub1.axis([1, 9, 1, 9])
        self.sub1.grid(True)
        plt.setp(self.sub1.get_xticklabels(), visible=False)
        plt.setp(self.sub1.get_yticklabels(), visible=False)
        self.sub1.tick_params(axis='both', which='both', length=0)

        data = self.genReport(self.chromosomes[1].genes)
       
        self.sub2 = plt.subplot(2, 2, 2)
     
        self.line2, = self.sub2.plot(data[0], data[1], "ro")
        self.sub2.axis([1, 9, 1, 9])
        self.sub2.grid(True)
        plt.setp(self.sub2.get_xticklabels(), visible=False)
        plt.setp(self.sub2.get_yticklabels(), visible=False)
        self.sub2.tick_params(axis='both', which='both', length=0)

    
        

        data = self.genReport(self.chromosomes[2].genes)
       
        self.sub3 = plt.subplot(2, 2, 3)
     
        self.line3, = self.sub3.plot(data[0], data[1], "ro")
        self.sub3.axis([1, 9, 1, 9])
        self.sub3.grid(True)
        plt.setp(self.sub3.get_xticklabels(), visible=False)
        plt.setp(self.sub3.get_yticklabels(), visible=False)
        self.sub3.tick_params(axis='both', which='both', length=0)


        data = self.genReport(self.chromosomes[3].genes)
       
        self.sub4 = plt.subplot(2, 2, 4)
     
        self.line4, = self.sub4.plot(data[0], data[1], "ro")
        self.sub4.axis([1, 9, 1, 9])
        self.sub4.grid(True)
        plt.setp(self.sub4.get_xticklabels(), visible=False)
        plt.setp(self.sub4.get_yticklabels(), visible=False)
        self.sub4.tick_params(axis='both', which='both', length=0)

        self.axbox = plt.axes([0.1, 0.01, 0.4, 0.05])
        self.text_box = TextBox(self.axbox, 'Generation', initial="10")
        #text_box.on_submit(submit)

        self.axbutton = plt.axes([0.81, 0.01, 0.04, 0.05])
        self.button = Button(self.axbutton, 'ok')
        self.button.on_clicked(self.run)

        self.axCheck = plt.axes([0.7, -0.03, 0.07, 0.15], zorder=-1, frameon=False)
        self.check = CheckButtons(self.axCheck, ["Mutation"], [0])
        plt.show()