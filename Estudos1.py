nome = input("Qual é o seu nome? ") # Pergunta o nome e armazena na variavel "nome"
print() # Pula uma linha
idade = input("Qual é a sua idade? ") # Pergunta a idade e armazena na variavel "idade"
print()
print("Olá,", nome) # Mostra um texto e o que esta na variavel "nome"
print()
aniversario = input(f"Ei {nome}, você disse que tem {idade} anos. Que dia você faz aniversário? ") # Pergunta o dia do aniversário e guarda na variavel "aniversario"
print()
print(f"Que legal, {nome}! Então você faz aniversário no dia {aniversario}!") # Mostra uma menssagem usando as variaveis "nome" e "aniversario"
