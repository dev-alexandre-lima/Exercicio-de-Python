#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

b = float(input('Informe o lado do quadrado: '))

a = b * b
dobro = a * 2

print('A área de um quadrado {:.2f} e o seu dobro {:.2f}.'.format(a, dobro))