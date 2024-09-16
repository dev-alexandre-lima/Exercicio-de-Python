#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Quanto você por hora? R$ "))
horas_trabalhadas = int(input("Quantas horas você trabalha no mês? "))

mensal = hora * horas_trabalhadas

print(f"O usuário recebe por hora {hora}R$ de {horas_trabalhadas}horas mensal no final do mês vai recebr {mensal}RS$!")
