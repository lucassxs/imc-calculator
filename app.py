altura = float(input("Digite a sua altura em cm:  "))
peso = float(input("Digite o seu peso em kg:  "))


## Adicionando o cálculo do IMC
IMC = altura / (peso/100)**2

print(f"Seu IMC é {IMC}")