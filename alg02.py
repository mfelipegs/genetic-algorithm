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
        self.melhores_individuos=[]

    def avaliar_individuo(self, x, y):
        return 20 + (x*x) + (y*y) - 10 * ((math.cos(2*math.pi*x)) + math.cos(2*math.pi*y))

    def criar_populacao(self):
        for i in range (self.tam_populacao):
            x = random.randint(self.interval_min, self.interval_max)
            y = random.randint(self.interval_min, self.interval_max)
            fitness = self.avaliar_individuo(x, y)
            individuo=[x, y, fitness]
            self.populacao.append(individuo)

    def selecionar_pai(self):
        pos_cand1 = random.randint(0, 49)
        pos_cand2 = random.randint(0, 49)

        pos_pai = 0;
        if (self.populacao[pos_cand1][2] > self.populacao[pos_cand2][2]):
            pos_pai = pos_cand1
        else:
            pos_pai = pos_cand2

        return pos_pai

    def realizar_mutacao(self, filho):
        valorx = random.randint(0, 100)
        valory = random.randint(0, 100)

        #se for menor ou igual a 1 significa que terá mutação (1%)
        if (valorx <= self.mutacao):
            filho[0] = random.randint(self.interval_min, self.interval_max)
        if(valory <= self.mutacao):
            filho[1] = random.randint(self.interval_min, self.interval_max)

        return filho

    # def realizar_descarte(self):
    #     self.populacao = sorted(self.populacao, key=lambda x:x[3])
    #     ind=1
    #     while ind <= self.num_filhos:
    #         del self.populacao[0]
    #         ind += 1

    def realizar_descarte(self, individuos):
        individuos = sorted(individuos, key=lambda x:x[2], reverse=True)
        self.populacao = individuos[:self.tam_populacao]

    def reproduzir(self):
        # precisa repetir 7 vezes o processo porque gera 2 filhos a cada reproducao, e precisa de 14
        f=1
        while f <= 13:
            #preciso de 2 pais
            pos_pai1 = self.selecionar_pai()
            pos_pai2 = self.selecionar_pai()

            #pro filho1 pego x do pai1, y do pai2, z do pai1
            xf1 = self.populacao[pos_pai1][0]
            xf2 = self.populacao[pos_pai2][0]
            yf1 = self.populacao[pos_pai2][1]
            yf2 = self.populacao[pos_pai1][1]
            fitnessf1 = self.avaliar_individuo(xf1, yf1)
            fitnessf2 = self.avaliar_individuo(xf2, yf2)

            filho1 = [xf1, yf1, fitnessf1]
            filho2 = [xf2, yf2, fitnessf2]

            #antes de add, verifico se tem mutação
            filho1 = self.realizar_mutacao(filho1)
            filho2 = self.realizar_mutacao(filho2)

            self.filhos.append(filho1)
            self.filhos.append(filho2)

            f += 1

    def verificar_melhor_individuo(self):
        #posicao 19 pq e 20 elementos
        #self.melhores_individuos.append([self.populacao[19][0], self.populacao[19][1], self.populacao[19][2]])
        # melhor_individuo = self.populacao[len(self.populacao) - 1]
        # self.melhores_individuos.append(melhor_individuo)

        # fig, ax = plt.subplots()
        # ax.plot(melhor_individuo[0], melhor_individuo[1], melhor_individuo[2])
        # plt.show()

        print("O melhor indivíduo: ")
        print("x = ", self.populacao[19][0])
        print("y = ", self.populacao[19][1])
        print("fitness = ", self.populacao[19][2])

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

ag = AlgoritmoGenetico()
ag.iniciar_execucao()