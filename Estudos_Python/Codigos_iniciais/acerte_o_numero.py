import random

def pular_linha():
    print()

numero = random.randint(1, 10)
divisao = numero % 2

if divisao == 0:
    produto = "par"
else:
    produto = "ímpar"

pular_linha()

chute = int(input(f"Qual é o número que eu pensei?. "))

pular_linha()

while chute != numero:
    if chute < numero:
        print(f"Você errou!")
        print(f"O número é maior e {produto}.")
        pular_linha()
        chute = int(input(f"Qual é o número que eu pensei? "))
        pular_linha()
    else:
        print(f"Você errou!")
        print(f"O número é menor e {produto}.")
        pular_linha()
        chute = int(input(f"Qual é o número que eu pensei? "))
        pular_linha()

print(f"Você acertou! o número é {numero}")
pular_linha()
