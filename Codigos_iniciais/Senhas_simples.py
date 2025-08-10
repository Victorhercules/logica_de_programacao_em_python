
# Cria uma função para pular uma linha
def pular_linha():
    print()

# Cria uma senha e garante que não será vazia
senha_criada = input("Crie uma senha: ")
while senha_criada == "":
    pular_linha()
    print("A senha não pode ser vazia!")
    senha_criada = input("Crie uma senha: ")

pular_linha()

# Garante que a senha digitada não está vazia ou errada
senha_digitada = input("Digite sua senha para entrar: ")
while senha_digitada == "" or senha_digitada != senha_criada:
    if senha_digitada == "":
        pular_linha()
        print("Você não digitou a senha!")
    else:
        pular_linha()
        print("Senha incorreta!")
    senha_digitada = input("Digite sua senha para entrar: ")
pular_linha()
print("Senha correta!")
