#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7

h = float(input('Digite sua altura: '))
genero = input('Digite H para homen e M para mulher')

if 'Hh' in genero:
    peso_ideal = (72.7*h) - 58
else:
    peso_ideal = (62.1*h) - 44.7

print(f'O seu peso ideal é {peso_ideal}')