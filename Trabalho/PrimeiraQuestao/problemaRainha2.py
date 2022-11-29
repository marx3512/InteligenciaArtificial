import random

positions = [0,0,0,0,0,0,0,0]

geracao = []

for i in range(3):
    for j in range(8):
        positions[j] = random.randint(0,7)
    print(positions)
    geracao.append(positions)
    
print(geracao)