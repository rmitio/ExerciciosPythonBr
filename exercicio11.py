#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    #o produto do dobro do primeiro com metade do segundo .
    #a soma do triplo do primeiro com o terceiro.
    #o terceiro elevado ao cubo.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real: '))

produto = (n1 * 2) * (n2 / 2)
soma_triplo = (n1 * 3) + real
real_ao_cubo = real * real * real
print('-' * 30)
print(f'O resultado do dobro do {n1} multiplicado com metado de {n2} é {produto}')
print(f'A soma do tripo de {n1} mais o {real} é {soma_triplo}')
print(f'O número {real} ao cubo é {real_ao_cubo}')
