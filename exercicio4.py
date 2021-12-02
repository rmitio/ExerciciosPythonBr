#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = []
for a in range(1, 5):
    nota = int(input(f'Digite a nota do {a}º Bimestre: '))
    notas.append(nota)

media = sum(notas) / 4
print(media)