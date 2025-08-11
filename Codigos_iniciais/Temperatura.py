# Guarda a temperatura digitada na variável "temperatura"
temperatura = int(input("Digite a temperatura: "))

# Define a variável de acordo com a temperatura
if temperatura < (18):
    variacao_temperatura = ("Frio")
elif temperatura >= 18 and  temperatura <= 25:
    variacao_temperatura = ("Agradável")
else:
    variacao_temperatura = ("Quente")
print(f"O clima está: {variacao_temperatura}")