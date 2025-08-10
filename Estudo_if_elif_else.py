idade = int(input("Qual sua idade? "))
print()
if idade < 18:
    print("Você é menor de idade")
elif idade >= 18 and idade < 65:
    print("Você é maior de idade") 
elif idade > 100:
    print("Você acha que me engana") 
else:
    print("Você é idoso")