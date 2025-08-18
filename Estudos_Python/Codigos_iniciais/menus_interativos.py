import datetime
import random

def resposta_saiu():
    print()

def erro_resposta():
    print(f"\nErro: Não é uma reposta válida!")

def menu_dado():
    while True:
        resposta_string = input("\nEscolha uma das opções abaixo:\n\n1 - Rolar um D6\n2 - Rolar um D20\n3 - Rolar um d50\n4 - Rolar um D100\n5 - Sair\n\n==> ")
        if resposta_string.isdigit():
            resposta_numero = int(resposta_string)
            if 0 < resposta_numero < 6:
                if 1 == resposta_numero:
                    dado = random.randint(1, 6)
                elif 2 == resposta_numero:
                    dado = random.randint(1, 20)
                elif 3 == resposta_numero:
                    dado = random.randint(1, 50)
                elif 4 == resposta_numero:
                    dado = random.randint(1, 100)
                else:
                    resposta_saiu()
                if 0 < resposta_numero < 5:
                    print(f"\nO resultado do dado foi: {dado}\n")
                break
        erro_resposta()

def menu_principal():
    while True:
        resposta_string = input("\nEscolha uma das opções abaixo:\n\n1 - Mostrar as horas\n2 - Rolar um dado\n3 - Sair\n\n==> ")
        if resposta_string.isdigit():
            resposta_numero = int(resposta_string)
            if 0 < resposta_numero < 4:
                if 1 == resposta_numero:
                    hora_atual = datetime.datetime.now()
                    hora_atual = hora_atual.strftime("%H:%M:%S")
                    print(f"\nAgora são: {hora_atual}\n")
                elif 2 == resposta_numero:
                    menu_dado()
                else:
                    resposta_saiu()
                break
        erro_resposta()

menu_principal()
