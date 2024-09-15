#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input('Informe a altura do usuário: '))

homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

print('O peso ideal {:.2f} para homens de {:.2f}'.format(homens, altura))
print('O peso ideal {:.2f} para mulheres de {:.2f}'.format(mulheres, altura))