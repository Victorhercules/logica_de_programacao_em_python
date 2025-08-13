# importa a biblioteca
import random

# cria uma função para pular uma linha
def pular_linha():
    print()

# cria uma função que pede um número e garante que é um número
def validar():
    pular_linha()
    chute_t = input("Qual é o número que eu pensei? ")
    while not chute_t.isdigit():
        print("Você não digitou um número")
        pular_linha()
        chute_t = input("Qual é o número que eu pensei? ")
    chute_n = int(chute_t)
    return chute_n

# define as variáveis
chute_n = validar()
numero = random.randint(1, 10)
divisao = numero % 2
vidas = 4

# descobre se o número aleatório é ímpar ou par
if divisao == 0:
    produto = "par"
else:
    produto = "ímpar"

pular_linha()

# cria um loop onde o usuário tem 5 chances de acertar
while chute_n != numero and vidas != 0:
    if chute_n < numero:
        vidas = vidas - 1
        tamanho = "maior"
    else:
        vidas = vidas - 1
        tamanho = "menor"
    print(f"Você errou!")
    pular_linha()
    print(f"O número é {tamanho} e {produto}.")
    chute_n = validar()
    pular_linha()

# define se ele acertou ou não
if chute_n == numero:
    print(f"Você acertou! O número é {numero}")
else:
    print(f"Você perdeu! O número era {numero}")
pular_linha()
