import random

def validar():
    while True:
        entrada = input("Qual é o número (de 1 a 10) que eu pensei? ").strip()
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= 10:
                return numero
        print("Entrada inválida. Digite um número de 1 a 10.\n")

# Sorteia o número e define a paridade
numero = random.randint(1, 10)
paridade = "par" if numero % 2 == 0 else "ímpar"

vidas = 5
chute = validar()

while chute != numero and vidas > 1:
    vidas -= 1
    if chute < numero:
        print(f"Você errou! O número é maior e {paridade}.")
    else:
        print(f"Você errou! O número é menor e {paridade}.")
    print(f"Você tem {vidas} tentativa(s) restante(s).\n")
    chute = validar()

if chute == numero:
    print(f"\nVocê acertou! O número era {numero}")
else:
    print(f"\nVocê perdeu! O número era {numero}")
