# 1.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print(a, "é maior")
else:
    print(b, "é maior")






# 2.

 idade = int(input("Digite sua ideda"))
 if idade >=18:
     print("voce esta na maioridade.")
 else:
     print("voce esta menoridade")]





# 3.

# solicita que o usuário informe seu nome e idade
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# verifica se o usuário pode dirigir
if idade >= 18:
    print("Olá,", nome, "! Você tem", idade, "anos e já pode dirigir um veículo.")
else:
    print("Desculpe,", nome, ", você só poderá dirigir quando completar 18 anos.")






# 4.

     n1 = float(input("Digite a primeira nota: "))
     n2 = float(input("Digite a segunda nota: "))
     n3 = float(input("Digite a terceira nota: "))
     n4 = float(input("Digite a quarta nota: "))

     media = (n1 + n2 + n3 + n4) / 4

     # verifica se o aluno foi aprovado ou reprovado
     if media >= 7:
         print("Parabéns, você foi aprovado com média", media)
     else:
         print("Infelizmente, você foi reprovado com média", media)



# 5.
     num = float(input("Digite um número: "))

     if num >= 0:
         print("O número é positivo!")
     else:
         print("O número é negativo!")]



# 6.
     salario = float(input("Digite o salário do funcionário: "))

     if salario > 1500:
         aumento = "salario" * 0.10:
     else:
         aumento = 'salario' * 0.15:

     novo_salario = "salario" + "aumento"

     print("O salário antigo era R${:.2f} e o aumento foi de R${:.2f}.".format(salario, aumento))
     print("O novo salário é R${:.2f}.".format(novo_salario))



#7
     numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()
     numeros = [int(num) for num in numeros]

     maior = numeros[0]
     menor = numeros[0]

     for num in numeros:
         if
     num > maior:
     maior = num
     if num < menor:
         menor = num

     print("O maior número é:", maior)
     print("O menor número é:", menor)



     #9 Laço externo para percorrer de 1 a 10

for i in range(1, 11):
    print(f"Tabuada do {i}:")

    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()



#10.

     nomes = input("Digite uma lista de nomes separados por espaço: ").split()

     # Cria um dicionário vazio
     nomes_unicos = {}

     # Adiciona cada nome como chave no dicionário
     # O valor associado à chave é irrelevante, pode ser None
     for nome in nomes:
         nomes_unicos[nome] = None

     # Converte o dicionário de volta para uma lista de nomes
     lista_nomes_unicos = list(nomes_unicos.keys())

     print("Lista de nomes sem duplicatas:", lista_nomes_unicos)

