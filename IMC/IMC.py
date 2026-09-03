peso = float(input("Digite o seu peso em kg (Se for quebrado, use ponto no lugar da vírgula)\n"))
altura = float(input("Digite a sua altura em metros.\n"))
imc = peso/(altura**2)

print(f"Seu IMC é de: {imc:.2f}")