import random

def pular_linha():
    print()

numero = random.randint(1, 10)

pular_linha()

chute = int(input("Qual é o número que eu pensei? "))
pular_linha()
while chute != numero:
        print(f"Você errou!")
        pular_linha()
        chute = int(input("Qual é o número que eu pensei? "))
        pular_linha()

print(f"Você acertou! o número é {numero}")
pular_linha()
