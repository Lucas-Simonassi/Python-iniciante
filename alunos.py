alunos = int(input("Quantos alunos a turma tem? "))

maior_nota = 0
nome_maior_nota = ''

for i in range(1, alunos+1):
    nome = input(f"Nome do aluno {i}: ")
    nota = float(input(f"Nota de {i}: "))
if nota > maior_nota:
    maior_nota = nota
    nome_maior_nota = nome

print(f' A maior nota foi de {nome_maior_nota} com {maior_nota} pontos: ' )
