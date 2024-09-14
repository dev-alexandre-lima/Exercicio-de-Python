#Desenvolva um programa que realize cálculos simples, como a soma, subtração, multiplicação e divisão de dois números inseridos pelo usuário.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2

print('A soma deu {}, a sua subtração deu {}.'.format(soma, subtração))
print('A multiplicação deu {}, a sua divisão deu {:.2f}.'.format(multiplicação, divisão))