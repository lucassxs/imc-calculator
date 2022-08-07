altura = float(input("Digite a sua altura em cm:  "))
peso = float(input("Digite o seu peso em kg:  "))


## Adicionando o cálculo do IMC
IMC = altura / (peso/100)**2

print(f"Seu IMC é {IMC}")

## Tabela de IMC

if IMC <= 18.4:
    print("Abaixo do peso")
elif IMC <= 24.9:
    print("Peso Normal")
elif IMC <= 29.9:
    print("Sobrepeso") 
elif IMC <= 34.9:
    print("Obesidade Grau I")
elif IMC <= 39.9:
    print("Obesidade Grau II")   
else:
    print("Obsesidade Grau III ou Mórbida")
