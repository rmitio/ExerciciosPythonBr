#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

F = int(input('Digite os graus em Fahrenheit: '))

C = 5 * ((F-32) / 9)

print(f'{F}ºF é igual a {C:.2f}ºC ')