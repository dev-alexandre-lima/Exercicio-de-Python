#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeira_nota = float(input("Primeira nota: "))
segunda_nota = float(input("Segunda nota: "))
terceira_nota = float(input("Terceira nota: "))
quarta_nota = float(input("Quarta nota: "))

soma_notas = primeira_nota +  segunda_nota + terceira_nota + quarta_nota
média_notas = soma_notas / 2

print("A soma das notas foi {} e a sua média é {:.1f}.".format(soma_notas, média_notas))