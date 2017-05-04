import random

class CommessoViaggiatore:

    def __init__(self, graph, population, pmut):
        self.graph = graph
        self.population = sorted(population, key=self.fitnes)
        self.pmut = pmut

    def fitnes(self, chromosome):
        fitness = 0
        for i in range(1,len(chromosome)):
            fitness += self.graph[int(chromosome[i-1])][int(chromosome[i])]
        return fitness

    def crossover(self, ca, cb):
        i, j = random.sample(range(0,len(ca)), 2)
        
        if i > j: i,j = j,i

        child = ''
        for k in cb:
            if len(child) == i:
                child += ca[i:j]
            if k not in ca[i:j]:
                child += k

        return child
            

    def mutation(self, chromosome):
        i, j = random.sample(range(0,len(chromosome)), 2)
        chromosome = list(chromosome)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return ''.join(chromosome)

    def evolve(self, gen):
        for j in range(gen):
            for i in range(int(len(self.population) * (2/3))):
                while True:
                    father, mother = random.sample(range(0,len(self.population)), 2)
                    child = self.crossover(self.population[father], self.population[mother])

                    if random.randint(0,1) < self.pmut:
                        child = self.mutation(child)

                    if child not in self.population: break
                
                if len(self.population) > 300: self.population[-i-1] = child
                else: self.population.append(child)

            self.population = sorted(self.population, key=self.fitnes)
            print("generation {0}: {1}".format(j, self.population))
            print("Best: {0}, fitness: {1}".format(self.population[0], self.fitnes(self.population[0])))

        return self.population[0]


cv = CommessoViaggiatore(
    [[0,2,3,4,5,6,7,8,9],
     [5,0,2,5,9,2,4,99,8],
     [3,7,0,8,5,6,6,3,2],
     [3,98,7,0,6,7,4,6,5],
     [3,7,7,8,0,12,4,6,5],
     [44,7,7,8,6,0,4,6,5],
     [3,0,7,8,6,7,0,9,5],
     [3,6,1,8,6,7,4,0,4],
     [3,7,2,8,5,7,4,3,0]],
     ['172536480', '012345678', '876540321', '182736450', '108245367', '182736450', '108243756', '162345870'],
     .4
)

print(cv.evolve(1000))