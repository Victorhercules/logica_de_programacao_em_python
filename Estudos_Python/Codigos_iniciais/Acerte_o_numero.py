import random

def validar():
    chute_string = input("\nQual é o número (de 1 a 10) que eu pensei? ")
    while not chute_string.isdigit():
        print("Você não digitou um número!\n")
        chute_string = input("Qual é o número (de 1 a 10) que eu pensei? ")
    chute_numero = int(chute_string)
    while chute_numero > 10 or chute_numero < 1:
        print("Você precisa digitar um número de 1 a 10!\n")
        chute_string = input("Qual é o número (de 1 a 10) que eu pensei? ")
        while not chute_string.isdigit():
            print("Você não digitou um número!\n")
            chute_string = input("Qual é o número (de 1 a 10) que eu pensei? ")
        chute_numero = int(chute_string)
    return chute_numero

numero = random.randint(1, 10)
divisao_numero = numero % 2
vidas = 5
chute_numero = validar()

if divisao_numero == 0:
    produto = "par"
else:
    produto = "ímpar"

while chute_numero != numero and vidas > 0:
    vidas -= 1
    if vidas == 0:
        break
    elif chute_numero < numero:
        print(f"Você errou! O número é maior e {produto}.\n")
    else:
        print(f"Você errou! O número é menor e {produto}\n.")
    print(f"Você tem {vidas} tentativas.")
    chute_numero = validar()

if chute_numero == numero:
    print(f"\nVocê acertou! O número é {numero}\n")
else:
    print(f"\nVocê perdeu! O número era {numero}\n")
