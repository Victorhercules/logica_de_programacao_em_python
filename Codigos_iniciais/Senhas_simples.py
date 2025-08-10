# Cria uma senha e garante que não será vazia
senha_criada = input("Crie uma senha: ")
while senha_criada == "":
    print("A senha não pode ser vazia!")
    senha_criada = input("Crie uma senha: ")

print()

# Garante que a senha digitada não está vazia ou errada
senha_digitada = input("Digite sua senha para entrar: ")
while senha_digitada == "" or senha_digitada != senha_criada:
    if senha_digitada == "":
        print("Você não digitou a senha!")
    else:
        print("Senha incorreta!")
    senha_digitada = input("Digite sua senha para entrar: ")

print("Senha correta!")
