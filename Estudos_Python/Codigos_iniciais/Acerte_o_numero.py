import random

def pular_linha():
    print()

def validar():
    pular_linha()
    print(f"Você tem {vidas + 1} tentativas.")
    chute_string = input("Qual é o número que eu pensei? ")
    while not chute_string.isdigit():
        print("Você não digitou um número")
        pular_linha()
        chute_string = input("Qual é o número que eu pensei? ")
    chute_numero = int(chute_string)
    return chute_numero

numero = random.randint(1, 10)
divisao_numero = numero % 2
vidas = 4
chute_numero = validar()

if divisao_numero == 0:
    produto = "par"
else:
    produto = "ímpar"

pular_linha()

while chute_numero != numero and vidas != 0:
    if chute_numero < numero:
        vidas = vidas - 1
        tamanho = "maior"
    else:
        vidas = vidas - 1
        tamanho = "menor"
    print(f"Você errou!")
    pular_linha()
    print(f"O número é {tamanho} e {produto}.")
    chute_numero = validar()
    pular_linha()

if chute_numero == numero:
    print(f"Você acertou! O número é {numero}")
else:
    print(f"Você perdeu! O número era {numero}")
pular_linha()
