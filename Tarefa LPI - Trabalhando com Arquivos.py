import os

for arquivo_nome in ["notas.txt", "aprovados.txt", "exame.txt", "reprovados.txt"]:
    with open(arquivo_nome, "w") as f:
        pass

dados_alunos = {} #Cria dicionário vazio para armazenar dados conforme o aluno

for aluno in range(1,4):
    nome = input(f"Qual o nome do {aluno}° aluno?\n")
    dados_alunos[nome] = [] #Cria chave com lista vazia

    for n in range(1,4): #Loop para armazenar notas do aluno
        nota = float(input(f"Qual a {n}° nota?\n"))
        dados_alunos[nome].append(nota)

with open("notas.txt", "w") as arquivo:

    for nome, notas in dados_alunos.items():
        linha = f"{nome}, {notas[0]}, {notas[1]}, {notas[2]}\n"
        arquivo.write(linha)

with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        dados_linha = linha.split(",")
        nomeArquivo = dados_linha[0]

        total_nota = 0

        for n in dados_linha[1:]:
            total_nota += float(n)

        media = total_nota/len(dados_linha[1:])

        if media >= 7:
            status = "Aprovado"
        elif 7 > media >= 5:
            status = "Exame"
        else:
            status = "Reprovado"

        if status == "Aprovado":
            with open("aprovados.txt", "a") as arquivo:
                arquivo.write(f"{nomeArquivo}. Média: {media:.2f}\n")
        elif status == "Exame":
            with open("exame.txt", "a") as arquivo:
                arquivo.write(f"{nomeArquivo}, {media:.2f}\n")
        else:
            with open("reprovados.txt", "a") as arquivo:
                arquivo.write(f"{nomeArquivo}. Média: {media:.2f}\n")
try:
    with open("exame.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            dados_linha = linha.split(",")
            nomeArquivo = dados_linha[0]
            media = float(dados_linha[1])
            media_exame = float(input(f"Qual foi a nota do {nomeArquivo} no exame?\n"))
            nova_media = (media + media_exame)/2

            if nova_media >= 5:
                status = "Aprovado"
                with open("aprovados.txt", "a") as arquivo:
                    arquivo.write(f"{nomeArquivo}, aprovado após exame. Média: {nova_media:.2f}\n")

            else:
                status= "Reprovado"
                with open("reprovados.txt", "a") as arquivo:
                    arquivo.write(f"{nomeArquivo}, reprovado após exame. Média: {nova_media:.2f}\n")

except FileNotFoundError:
    print("Nenhum aluno ficou de exame, logo o arquivo exame.txt não foi gerado.")

print("\nAlunos aprovados:")
with open("aprovados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print("Alunos reprovados:")
with open("reprovados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
