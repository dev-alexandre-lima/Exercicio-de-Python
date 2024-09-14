#Crie um programa que solicite ao usuário informações como nome, idade e altura, e utilize essas variáveis para exibir uma mensagem personalizada.

nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))
altura = float(input("Qual a sua altura? "))

print("Olá, {}! Você tem {} anos e a sua altura é {}.".format(nome, idade, altura))
