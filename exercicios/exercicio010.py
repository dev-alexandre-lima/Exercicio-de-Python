#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

#Leve em conta que o salário mínimo atual de 2024 é de 1.412R$ e por hora o valor de R$6.42

sálrio_hora = float(input('Quanto você ganhar por hora? R$ '))
horas_trabalhadas = int(input('Quantas horas trabalhadas no mês? '))

salario = (sálrio_hora * horas_trabalhadas) / 2

print(salario)