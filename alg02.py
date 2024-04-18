import random
import math
import matplotlib.pyplot as plt

class AlgoritmoGenetico:
    def __init__(self):
        self.tam_populacao = 50
        self.populacao=[]
        self.num_geracoes=25
        self.num_filhos=36
        self.filhos=[]
        self.mutacao=4
        self.interval_min=-5
        self.interval_max=5
        self.melhor_individuo_x=[]
        self.melhor_individuo_y=[]
        self.melhor_individuo_z=[]

    def avaliar_individuo(self, x, y):
        return 20 + (x*x) + (y*y) - 10 * ((math.cos(2*math.pi*x)) + math.cos(2*math.pi*y))

    def criar_populacao(self):
        for i in range (self.tam_populacao):
            x = random.uniform(self.interval_min, self.interval_max)
            y = random.uniform(self.interval_min, self.interval_max)
            fitness = self.avaliar_individuo(x, y)
            individuo=[x, y, fitness]
            self.populacao.append(individuo)

    def selecionar_pai(self):
        pos_cand1 = random.randint(0, len(self.populacao) - 1)
        pos_cand2 = random.randint(0, len(self.populacao) - 1)

        pos_pai = 0;
        if (self.populacao[pos_cand1][2] < self.populacao[pos_cand2][2]):
            pos_pai = pos_cand1
        else:
            pos_pai = pos_cand2

        return pos_pai

    def realizar_mutacao(self, filho):
        valorx = random.randint(0, 100)
        valory = random.randint(0, 100)

        # mutação (1%)
        if (valorx <= self.mutacao):
            filho[0] = random.uniform(self.interval_min, self.interval_max)
        if(valory <= self.mutacao):
            filho[1] = random.uniform(self.interval_min, self.interval_max)

        return filho

    def realizar_descarte(self, individuos):
        individuos = sorted(individuos, key=lambda x:x[2], reverse=True)
        self.populacao = individuos[:self.tam_populacao]

    def reproduzir(self):
        f=1
        while f <= 13:
            # 2 pais
            pos_pai1 = self.selecionar_pai()
            pos_pai2 = self.selecionar_pai()

            # filho1 -> x do pai1, y do pai2, z do pai1
            xf1 = self.populacao[pos_pai1][0]
            xf2 = self.populacao[pos_pai2][0]
            yf1 = self.populacao[pos_pai2][1]
            yf2 = self.populacao[pos_pai1][1]
            fitnessf1 = self.avaliar_individuo(xf1, yf1)
            fitnessf2 = self.avaliar_individuo(xf2, yf2)

            filho1 = [xf1, yf1, fitnessf1]
            filho2 = [xf2, yf2, fitnessf2]

            # verificando se há mutação
            filho1 = self.realizar_mutacao(filho1)
            filho2 = self.realizar_mutacao(filho2)

            self.filhos.append(filho1)
            self.filhos.append(filho2)

            f += 1

    def verificar_melhor_individuo(self):
        self.melhor_individuo_x.append(self.populacao[len(self.populacao) - 1][0])
        self.melhor_individuo_y.append(self.populacao[len(self.populacao) - 1][1])
        self.melhor_individuo_z.append(self.populacao[len(self.populacao) - 1][2])

        print("O melhor indivíduo: ")
        print("x = ", self.populacao[len(self.populacao) - 1][0])
        print("y = ", self.populacao[len(self.populacao) - 1][1])
        print("fitness = ", self.populacao[len(self.populacao) - 1][2])

    def iniciar_execucao(self):
        self.criar_populacao()
        contador_geracoes = 1

        while contador_geracoes <= self.num_geracoes:
            print("---------------------")
            print("Geracao ", contador_geracoes)
            self.filhos = []
            self.reproduzir()
            self.populacao = self.populacao + self.filhos
            self.realizar_descarte(self.populacao)
            self.verificar_melhor_individuo()
            contador_geracoes += 1

        ax = plt.axes(projection="3d")
        ax.plot3D(self.melhor_individuo_x, self.melhor_individuo_y, self.melhor_individuo_z, "green")
        ax.set_title("Algoritmo 02")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Fitness")
        plt.show()

ag = AlgoritmoGenetico()
ag.iniciar_execucao()