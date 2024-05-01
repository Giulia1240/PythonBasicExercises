"""
5.Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D
segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

6.Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e
 calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas
trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade.
 No caso do salário, também deve haver um espaço em branco após o $.

7.Calcule a área do triangulo

8.Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e
o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores,
respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de
* deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado
* com 2 casas após o ponto.


9-Peça ao usuário digitar as seguintes informações:
    *O nome completo
    *A idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
     exiba "Desculpe, você deixou campos vazios

10-solicite a um usuario inserir a senha e o login e somente deve acessar quando a senha foi comaptivel a registrada no sistema
e a opção solicitar foi para entrar na plataforma.

"""
print("Exercise 5: ")

a = input("Insert the value for A attribute: ")
b = input("Insert the value for B attribute: ")
c = input("Insert the value for C attribute: ")
d = input("Insert the value for D attribute: ")

convertA = int(a)
convertB = int(b)
convertC = int(c)
convertD = int(d)

difference = (convertA * convertB) - (convertC * convertD)
print(f'DIFFERENCE: {difference}')

print("===================================================================================================")
print("Exercise 06: ")

horasTotaisPordia = input("Insira as horas totais diarias trabalhadas: ")

valorPorhora = 20.0
horasPadrao = 8.0
diastrabalhados = 22

valorTotalPorDia = float(horasTotaisPordia) * valorPorhora

if (float(horasTotaisPordia) > horasPadrao):
    horasExtra = float(horasTotaisPordia) - horasPadrao
    valorExtra = horasExtra * 1.5

    mensal = (valorTotalPorDia + valorExtra) * diastrabalhados
    formatingMensal = format(mensal, '.2f')
    print(formatingMensal)
else:
    mensal = valorTotalPorDia * diastrabalhados
    formatingMensal = format(mensal, '.2f')
    print(formatingMensal)

print("===================================================================================================")
print("Execise 7: ")

base = input("Insert the base value: ")
height = input("Insert the height value: ")

trianguleArea = (int(base) * int(height)) / 2

print(trianguleArea)

print("===================================================================================================")
print("Exercise 8: ")

options = input("Escolha o codigo do produto:1,2 ou 3:  ")
qtPeca = input("Digite a quantidade de pecas desejada: ")

code = int(options)
valorUnitarioPecaOne = 4.00
valorUnitarioPecaTwo = 5.00
valorUnitarioPecaThree = valorUnitarioPecaOne + valorUnitarioPecaTwo

totalValueOne = int(qtPeca) * valorUnitarioPecaOne
totalValueTwo = int(qtPeca) * valorUnitarioPecaTwo
totalValuethree = int(qtPeca) * valorUnitarioPecaThree

formatingOne = format(totalValueOne, '.2f')
formatingTwo = format(totalValueTwo, '.2f')
formatingThree = format(totalValuethree, '.2f')


def switch_case(argument):
    switch_func = {
        1: lambda: f'The product code is {code} and the total value is {formatingOne}',
        2: lambda: f'The product code is {code} and the total value is {formatingTwo}',
        3: lambda: f'The product code is {code} and the total value is {formatingThree}'
    }
    return switch_func.get(argument, lambda: "value not found.")()

print("===================================================================================================")
print("Exercise 9: ")

name=input("Insert your name: ")
if name:
    nameInverted=name[::-1]
    nameContem= len(name)
    primeiraLetra=name[0]
    segundaLetra=name[-1]
    contarEntreLetras=name[0:3]

    print(f'Seu nome é {name} \n')
    print(f'Seu nome invertido é {nameInverted} \n')
    print(f'Seu nome contém {nameContem} letras \n')
    print(f'A primeira letra do seu nome é {primeiraLetra} \n')
    print(f'A segunda letra do seu nome é {segundaLetra} \n')
    print(f'Teste {contarEntreLetras} \n')

    if(" " in name):
        print(f'O nome {name} contém espaço vazio')

    else:
        print(f'O nome {name} não contém espaço vazio')

else:
    print("Desculpe, você deixou campos vazios")

print("Exercise 10")

user= input("Insert your user: ")
password=input("Insert your password:" )
passd=int(password)
button=input("Select the option that you want to execute: \n [E]ntrar \n [S]air \n ")

userRegistrated="test"
passwordRegistred=123

if(user==userRegistrated and passd==passwordRegistred and button == "E" or button =="e"):
    print("Welcome to System")
elif(user==userRegistrated and passd==passwordRegistred and button == "S" or button=="s"):
    print("Exit")
else:
    print("user or password is incorrect, try again")


