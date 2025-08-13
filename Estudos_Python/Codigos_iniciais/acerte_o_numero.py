import random

def pular_linha():
    print()

numero = random.randint(1, 10)
divisao = numero % 2
vidas = 0

if divisao == 0:
    produto = "par"
else:
    produto = "ímpar"

pular_linha()

chute = int(input("Qual é o número que eu pensei? "))

pular_linha()

while chute != numero and vidas < 4:
    if chute < numero:
        vidas += 1
        tamanho = "maior"
    else:
        vidas += 1
        tamanho = "menor"
    print(f"Você errou!")
    pular_linha()
    print(f"O número é {tamanho} e {produto}.")
    pular_linha()
    chute = int(input(f"Qual é o número que eu pensei? "))
    pular_linha()


if vidas == 4:
    print(f"Você perdeu! O número era {numero}")
else:
    print(f"Você acertou! O número é {numero}")
pular_linha()
