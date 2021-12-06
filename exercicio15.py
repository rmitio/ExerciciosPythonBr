"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
"""

valor_hora = float(input('Digite seu valor hora: '))
horas_trabalhadas = int(input('Digite as horas trabalhadas: '))
bruto = valor_hora * horas_trabalhadas
IR = bruto * (11/100)
INSS = bruto * (8/100)
Sindicato = bruto * (5/100)
liquido = bruto - IR - INSS - Sindicato
print(f"""Salário Bruto: R${bruto:.2f}
IR: R${IR:.2f}
INSS: R${INSS:.2f}
Sindicato R${Sindicato:.2f}
Salário Liquido R${liquido:.2f} """)
