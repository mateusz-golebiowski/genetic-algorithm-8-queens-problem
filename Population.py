import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import TextBox
from matplotlib.backends.backend_pdf import PdfPages
from random import randint
import datetime

import Chromosome

class Population:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.selected = []
        self.generation = 0
        self.initialPopulation = self.chromosomes.copy()

        self.plots = []
        self.dots = []
        self.endGeneration = 10
        self.doMutation = False

        
        
    def run(self):
        self.showResult()

    def fitness(self):
        #print("Fitness computing...")
        for ch in self.chromosomes:
            ch.computeFitness()

    def selection(self):
        #print("Generation: {}".format(self.generation+1))
        self.selected = []
        for g in range(0,3):
            m = max([ i.fitness for i in self.chromosomes])
            added = False
            for ch in self.chromosomes:
                if ch.fitness == m and added == False: 
                    self.selected.append(ch)
                    self.chromosomes.remove(ch)
                    added = True
        #print("Selected chromosomes")
        show =[i.genes for i in self.selected]
        #print(show)
                    
    def crossover(self):
        #print("Crossover...")
        self.chromosomes = [
            Chromosome.Chromosome(self.selected[0].genes[:4]+self.selected[1].genes[4:]),
            Chromosome.Chromosome(self.selected[1].genes[:4]+self.selected[0].genes[4:]),
            Chromosome.Chromosome(self.selected[0].genes[:4]+self.selected[2].genes[4:]),
            Chromosome.Chromosome(self.selected[2].genes[:4]+self.selected[0].genes[4:]),

        ]
        #print("Population after crossover: ")
        
        #print([i.genes for i in self.chromosomes])

        self.generation +=1

    def mutation(self):
        #print("Mutation...")
        ch = randint(0, 3)
        gene = randint(0, 7)
        oldValue = self.chromosomes[ch].genes[gene]
        while oldValue == self.chromosomes[ch].genes[gene]:
            self.chromosomes[ch].genes[gene] = randint(1, 8)
        #print("Population after mutation")
        #print([i.genes for i in self.chromosomes])

    def genReport(self, genes):
        x = [1.5 ,2.5, 3.5, 4.5, 5.5, 6.5, 7.5 ,8.5]
        y =[ g+0.5 for g in genes ]

        return [x, y]


    def okButtonClicked(self,data):
        now = datetime.datetime.now()
        self.pp = PdfPages('result({}-{}-{} {}.{}.{}).pdf'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))
        
        self.axbutton.set_visible(False)
        self.axbox.set_visible(False)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        self.pp.savefig(self.fig)
        
        print([i.genes for i in self.chromosomes])

        self.fitness()

        while self.generation < self.endGeneration:
            self.selection()
            self.crossover()
            if self.doMutation:
                self.mutation()
            
            self.fitness()
            

        for i in range(0,4):
            data = self.genReport(self.chromosomes[i].genes)
            self.dots[i].set_ydata(data[1])
            self.chromosomes[i].computeFitness()
            self.plots[i].set_xlabel("Chromosome {}: {}\nFitness:{}".format(i+1,tuple(self.chromosomes[i].genes),self.chromosomes[i].fitness))
        self.fig.suptitle('{} Generation'.format(self.generation), fontsize=20)
        self.pp.savefig(self.fig)
        self.pp.close()

        self.axresbutton.set_visible(True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

        print([i.genes for i in self.chromosomes])
        
    def restartButtonClicked(self,data):
        self.chromosomes = self.initialPopulation.copy()
        
        for i in range(0,4):
            data = self.genReport(self.chromosomes[i].genes)
            self.dots[i].set_ydata(data[1])
            self.chromosomes[i].computeFitness()
            self.plots[i].set_xlabel("Chromosome {}: {}\nFitness:{}".format(i+1,tuple(self.chromosomes[i].genes),self.chromosomes[i].fitness))
        
        self.generation = 0
        self.endGeneration = 10
        #self.text_box.set_val(10)
        self.fig.suptitle('Initial Population', fontsize=20)
        self.axbutton.set_visible(True)
        self.axbox.set_visible(True)
        self.axresbutton.set_visible(False)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        


    def mutationCheckbox(self, label):
        self.doMutation = not self.doMutation

    def submit(self, text):
        self.endGeneration = int(text)

    def showResult(self):
        self.fig = plt.figure(figsize=(120, 60))
        self.fig.suptitle('Initial Population', fontsize=20)
        for i in range(0,4):
            data = self.genReport(self.chromosomes[i].genes)
            self.plots.append(plt.subplot(2, 2, i+1))
            line, = self.plots[i].plot(data[0], data[1], "ro")
            self.dots.append(line)
            self.plots[i].axis([1, 9, 1, 9])
            self.plots[i].grid(True)
            plt.setp(self.plots[i].get_xticklabels(), visible=False)
            plt.setp(self.plots[i].get_yticklabels(), visible=False)
            self.plots[i].tick_params(axis='both', which='both', length=0)
            self.chromosomes[i].computeFitness()
            self.plots[i].set_xlabel("Chromosome {}: {}\nFitness:{}".format(i+1,tuple(self.chromosomes[i].genes),self.chromosomes[i].fitness))

        self.axbox = plt.axes([0.1, 0.01, 0.2, 0.05])
        self.text_box = TextBox(self.axbox, 'Generation', initial="10")
        self.text_box.on_submit(self.submit)
        self.axbutton = plt.axes([0.81, 0.01, 0.04, 0.05])
        self.button = Button(self.axbutton, 'ok')
        self.button.on_clicked(self.okButtonClicked)

        self.axCheck = plt.axes([0.7, -0.03, 0.07, 0.15], zorder=-1, frameon=False)
        self.check = CheckButtons(self.axCheck, ["Mutation"], [0])
        self.check.on_clicked(self.mutationCheckbox)

        self.axresbutton = plt.axes([0.85, 0.01, 0.05, 0.05])
        self.restartButton = Button(self.axresbutton, 'Restart')
        self.restartButton.on_clicked(self.restartButtonClicked)
        self.axresbutton.set_visible(False)

        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')



        plt.show()