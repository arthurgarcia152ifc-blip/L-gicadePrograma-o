aluno_atual = 0
media_total = 0
alunos_aprovados = 0

for i in range(1, 11):
    aluno_atual = float(input("Qual a nota final do aluno: "))
    media_total += aluno_atual

    if aluno_atual >= 7:
        alunos_aprovados += 1

print("Média geral:", media_total / 10)
print("Alunos aprovados:", alunos_aprovados)