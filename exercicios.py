# 1) Faça um programa que leia dois números e mostre a soma, a subtração, a multiplicação e a divisão entre eles.
# num = float(input("Digite o primeiro número:"))
# num2 = float(input("Digite o segundo número:"))
# soma = num + num2
# sub = num - num2
# mult = num * num2 
# div = num / num2
# print(f"A soma dos números são: {soma}")
# print(f"A subtração dos números são: {sub}")
# print(f"A multiplicação dos números são: {mult}")
# print(f"A divisão dos números são: {div}")

# 2)  Faça um programa que solicite o ano de nascimento do usuário e calcule a sua idade.
# nasc = int(input("Digite o ano do seu nascimento:"))
# anoAtual = 2025
# idade = anoAtual - nasc
# print(f"A sua idade é: {idade}")

# 3) Crie um programa que leia um valor em reais (R$) e mostre o valor convertido em dólares (US$), considerando uma taxa de câmbio fornecida pelo usuário.
# valor = float(input("Digite um valor em R$:"))
# taxa = float(input("Digite a taxa de câmbio desejada para fazer a conversão:"))
# conversao = valor / taxa 
# print(f"O valor de R${valor} equivale a {conversao}")

# 4) Crie um programa que leia três notas de um aluno e calcule a média aritmética.
# nome = input("Digite o nome do aluno:")
# nota = float(input("Digite a primeira nota:"))
# nota2 = float(input("Digite a segunda nota:"))
# nota3 = float(input("Digite a terceira nota:"))
# media = (nota + nota2 + nota3) / 3
# print(f"A média do(a) {nome} é: {media:.1f}")

# 5) Escreva um programa que leia o valor de um produto e o percentual de desconto. O programa deve exibir o valor final com o desconto aplicado.
# produto = input("Digite o nome do produto:")
# valor = float(input("Digite o valor do produto:"))
# percentual = 0.20
# desconto= valor * percentual
# valorFinal = valor - desconto
# print(f"O desconto será de {desconto} e o valor do {produto} com desconto aplicado é: {valorFinal}")

# 6) Crie um programa que leia uma frase e mostre quantos caracteres ela possui (incluindo espaços).
# frase = input("Digite uma frase:")
# caracteres = len(frase)
# print(f"A frase {frase} possui {caracteres} caracteres (incluindo espaços).")

# 7) Escreva um programa que receba três números inteiros e determine qual deles é o maior.

# 8) Escreva um programa para ler o salário de um funcionário, e calcular o IRPF que precisa ser descontado do salário.
# No Brasil, a tabela do Imposto de Renda para pessoas físicas (IRPF) é progressiva, ou seja, as alíquotas aumentam conforme a renda do contribuinte. A tabela é ajustada anualmente e varia de acordo com a faixa de salário. Para o ano de 2024, as faixas de tributação do Imposto de Renda para pessoas físicas são as seguintes:
# Até R$ 2.112,00: isento (não paga imposto de renda)
# De R$ 2.112,01 até R$ 2.826,65: 7,5% (aplica-se sobre o valor que exceder a R$ 2.112,00)
# De R$ 2.826,66 até R$ 3.751,05: 15% (aplica-se sobre o valor que exceder a R$ 2.826,65)
# De R$ 3.751,06 até R$ 4.664,68: 22,5% (aplica-se sobre o valor que exceder a R$ 3.751,05)
# Acima de R$ 4.664,68: 27,5% (aplica-se sobre o valor que exceder a R$ 4.664,68)

# salario = float(input("Informe o salário do funcionário:"))
# if salario <= 2112:
#     irpf = 0
#     print("Isento")
# elif salario >= 2112.01 and salario <= 2826.65:
#     irpf = salario * 0.075
#     print(f"O valor descontado será {irpf:.2f}") 
# elif salario >=2826.66 and salario <= 3751.05:
#     irpf = salario * 0.15
#     print(f"O valor descontado será {irpf:.2f}")
# elif salario >= 3751.06 and salario <= 4664.68:
#     irpf = salario * 0.225
#     print(f"O valor descontado será {irpf:.2f}")
# else:
#     irpf = salario * 0.275
#     print(f"O valor descontado será {irpf:.2f}")

# 9) Crie um programa que calcule o valor total de uma compra feita em várias parcelas. Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma. Se o total ultrapassar R$ 1.000,00, acrescente 5% de juros.

# 10) Considere que o preço da tarifa de energia é R$ 0,50 por kWh. Pergunte ao usuário o consumo de energia em kWh e calcule o valor total a ser pago pela conta. Se o consumo for maior que 200 kWh, aplique um desconto de 10%.
# tarifa = 0.50
# consumo = float(input("Qual o seu consumo de energia por kWh?"))
# if consumo > 200:
#     percentual = consumo * 0.10
#     desconto = consumo - percentual
#     print(f"O valor total da conta com desconto é: {desconto}")
# else:
#     valor = tarifa * consumo
#     print(f"O valor total é: {valor}")

# 11) Crie um programa que calcule o tempo restante até a aposentadoria de uma pessoa. Pergunte a idade e o tempo de contribuição (em anos). A pessoa pode se aposentar com 35 anos de contribuição ou 60 anos de idade. Mostre o tempo restante para a aposentadoria

idade = int(input("Informe a sua idade:"))
tempo = float(input("Informe o tempo de contribuição (em anos):"))


# 12) ler 3 valores e verificar se podem ser lados de um triangulo e informar caso afirmativo, qual é o triangulo
num = float(input("Informe o primeiro número:"))
num2 = float(input("Informe o segundo número:"))
num3 = float(input("Informe o terceiro número:"))