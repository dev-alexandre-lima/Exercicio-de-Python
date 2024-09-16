#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# 1 - salário bruto.
# 2 - quanto pagou ao INSS.
# 3 - quanto pagou ao sindicato.
# 4 - o salário líquido.
# 5 - calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.

hora = float(input("Quanto você por hora? R$ "))
horas_trabalhadas = int(input("Quantas horas você trabalha no mês? "))

mensal = hora * horas_trabalhadas

print(f"O usuário recebe por hora {hora}R$ de {horas_trabalhadas}horas mensal no final do mês vai recebr {mensal}RS$!")
