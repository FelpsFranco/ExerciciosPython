#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
#média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.


nome = []
media = []
notas = []
acima_da_media = 0

for aluno in range(10):
    nomes = str(input('Nome do aluno: '))
    nome.append(nomes)
    i = 0
    while i < 4:
        i = i +1
        nota = float(input('Digite a {}° nota: '.format(i)))
        notas.append(nota)
    print('\nAluno: ',nome)
    print('Notas: ',notas)
    fazendo_media = sum(notas) / 4
    if fazendo_media > 70:
        acima_da_media = acima_da_media + 1
    media.append(fazendo_media)
    nome = []
    notas = []
    print('Média do Aluno: ',fazendo_media)

print(media)
print('Quantidade de alunos aprovados: ', acima_da_media)

