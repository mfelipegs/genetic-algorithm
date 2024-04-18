import random
import math
import matplotlib.pyplot as plt
from colors import GREEN

class AlgoritmoGenetico:
    def __init__(self):
        self.population_size = 50
        self.population=[]
        self.number_generations=25
        self.number_childs=36
        self.childs=[]
        self.mutation=4
        self.interval_min=-500
        self.interval_max=500
        self.best_individual_x=[]
        self.best_individual_y=[]
        self.best_individual_z=[]

    def avaliar_individuo(self, x1, x2):
        valor_x1 = x1 * math.sin(math.sqrt(abs(x1)))
        valor_x2 = x2 * math.sin(math.sqrt(abs(x2)))
        return 837.9658 - (valor_x1 + valor_x2)

    def criar_populacao(self):
        for i in range (self.population_size):
            x = random.uniform(self.interval_min, self.interval_max)
            y = random.uniform(self.interval_min, self.interval_max)
            fitness = self.avaliar_individuo(x, y)
            individuo=[x, y, fitness]
            self.population.append(individuo)

    def selecionar_pai(self):
        pos_cand1 = random.randint(0, len(self.population) - 1)
        pos_cand2 = random.randint(0, len(self.population) - 1)

        pos_pai = 0;
        if (self.population[pos_cand1][2] < self.population[pos_cand2][2]):
            pos_pai = pos_cand1
        else:
            pos_pai = pos_cand2

        return pos_pai

    def mutate_individual(self, child):
        value_x = random.randint(0, 100)
        value_y = random.randint(0, 100)

        # mutação (1%)
        if (value_x <= self.mutation):
            child[0] = random.uniform(self.interval_min, self.interval_max)
        if(value_y <= self.mutation):
            child[1] = random.uniform(self.interval_min, self.interval_max)

        return child

    def discard_unfit_individuals(self, individuals):
        individuals = sorted(individuals, key=lambda x:x[2], reverse=True)
        self.population = individuals[:self.population_size]

    def reproduzir(self):
        f=1
        while f <= 13:
            # 2 pais
            pos_pai1 = self.selecionar_pai()
            pos_pai2 = self.selecionar_pai()

            # filho1 -> x do pai1, y do pai2, z do pai1
            xf1 = self.population[pos_pai1][0]
            xf2 = self.population[pos_pai2][0]
            yf1 = self.population[pos_pai2][1]
            yf2 = self.population[pos_pai1][1]
            fitnessf1 = self.avaliar_individuo(xf1, yf1)
            fitnessf2 = self.avaliar_individuo(xf2, yf2)

            child1 = [xf1, yf1, fitnessf1]
            child2 = [xf2, yf2, fitnessf2]

            # verifying mutation
            child1 = self.mutate_individual(child1)
            child2 = self.mutate_individual(child2)

            self.childs.append(child1)
            self.childs.append(child2)

            f += 1

    def verificar_melhor_individuo(self):
        self.best_individual_x.append(self.population[len(self.population) - 1][0])
        self.best_individual_y.append(self.population[len(self.population) - 1][1])
        self.best_individual_z.append(self.population[len(self.population) - 1][2])

        print("O melhor indivíduo: ")
        print("x = ", self.population[len(self.population) - 1][0])
        print("y = ", self.population[len(self.population) - 1][1])
        print("fitness = ", self.population[len(self.population) - 1][2])

    def iniciar_execucao(self):
        self.criar_populacao()
        contador_geracoes = 1

        while contador_geracoes <= self.number_generations:
            print("---------------------")
            print("Geracao ", contador_geracoes)
            self.childs = []
            self.reproduzir()
            self.population = self.population + self.childs
            self.discard_unfit_individuals(self.population)
            self.verificar_melhor_individuo()
            contador_geracoes += 1

        ax = plt.axes(projection="3d")
        ax.plot3D(self.best_individual_x, self.best_individual_y, self.best_individual_z, GREEN)
        ax.set_title("Algoritmo 01")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Fitness")
        plt.show()

ag = AlgoritmoGenetico()
ag.iniciar_execucao()