#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora = int(input('Digite o valor da sua hora: \n'))
qtd_horas = int(input('Digite a quantidade de horas trabalhadas no mês: \n'))

salario = valor_hora * qtd_horas

print(f'Seu salario é R${salario:.2f}')