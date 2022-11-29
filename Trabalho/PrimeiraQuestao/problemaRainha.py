import uuid, random

class Tabuleiro:
    tabuleiro = [ [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0, 0, 0] ]
    
    def __init__(self, generation):
        self.id = uuid.uuid4()
        self.generation = generation
        self.positions = self.generatePositions()
        self.generateBoard(self.positions)
    
    def generateBoard(self, positions):
        for i in range(8):
            for j in range(8):
                if i == positions[j]:
                    self.tabuleiro[i][j] = 1
    
    def generatePositions(self):
        postions = []
        for i in range(8):
            postions.append(random.randint(0,7))
        
        return postions
    
    def showTab(self):
        for i in range(8):
            for j in range(8):
                print(self.tabuleiro[i][j], end = " ")
            print()
    
    def drainOutTab(self):
        for i in range(8):
            for j in range(8):
                self.tabuleiro[i][j] = 0
    
    def getNumberNoAttack(self):
        numberAttack = 0
        
        for j in range(0,8):
            row =  self.tabuleiro[j]
            indexRow = self.positions[j]
            numberAttack += self.checkRow(row)
            numberAttack += self.checkDiagonalUp(j, indexRow)
            numberAttack += self.checkDiagonalDown(j, indexRow)
        return 28 - numberAttack
    
    def checkRow(self, row):
        numberAttackRow = 0
        
        for i in range(0,8):
            if row[i] == 1:
                numberAttackRow += 1
        
        if numberAttackRow == 1:
            return 0
        else:
            return numberAttackRow

    def checkDiagonalUp(self, indexElement, row):
        numberAttackDiagonUp = 0
        
        for i in range(indexElement + 1, 8):
            row -= 1
            if row < 0:
                break
            elif self.tabuleiro[row][i] == 1:
                numberAttackDiagonUp += 1
        
        return numberAttackDiagonUp

    def checkDiagonalDown(self, indexElement, row):
        numberAttackDiagonUp = 0
        
        for i in range(indexElement + 1, 8):
            row += 1
            if row > 7:
                break
            elif self.tabuleiro[row][i] == 1:
                numberAttackDiagonUp += 1
        
        return numberAttackDiagonUp
        
def PopulationGeneration100():
    population = []
    positions = []
    
    for i in range(10):
        positions.clear()
        for j in range(8):
            positions.append(random.randint(0,7))
        tabuleiro = Tabuleiro(i + 1)
        print(tabuleiro)    
        tabuleiro.drainOutTab()
        print("-----------")
        
    Fitness(population)

def Fitness(population):
    totalAttack = 0
    
    for i in range(len(population)):
        totalAttack += population[i].getNumberNoAttack()
        population[i].showTab()
        print(totalAttack)

    return totalAttack;
    
    


# tabuleiro = Tabuleiro(1,[0,1,2,3,4,5,6,7])
# tabuleiro.showTab()
# print(tabuleiro.getNumberNoAttack())
PopulationGeneration100()