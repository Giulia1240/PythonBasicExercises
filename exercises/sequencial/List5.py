"""
17-Faça um programa que leia todos os numeros enquanto seja n for menor que 10 e sempre ignore
numeros pares
18-Construa um programa que a quantidade de colunas seja o equivalente a quantidade de linhas de forma que coluna E linha
19-Retorne o qualquer nome por meio do seguinte modelo: N*o*m*e
20-Faça um programa que converta tudo que for maiusculo para minusculo.
21-Crie uma calucladora no qual calcule numeros flutuantes ate 2 casas decimais
"""

print("Exercise 17: ")
contador=0

while contador<10:
    contador+=1
    if contador%2==0:
        print(f'{contador} é par, portanto, será ignorado')
        continue
    print(contador)


print("Execise 18: ")
qtLinha=5
qtColuna=5

linha=1
while linha <=qtLinha:
    coluna=1
    while coluna <=qtColuna:
        print(f'{linha=}{coluna=}')
        coluna+=1
    linha+=1

print("Exercise 19:")

name = input("Digite qualquer nome: ")
indice = 0
new_name = ''

while indice < len(name):
    letter = name[indice]
    new_name += f'*{letter}'
    indice += 1

new_name += '*'
print(new_name)

print("Exercise 20: ")

while True:
        button= input("Deseja sair? [s]im [n]ao: ")
        button=button.lower()
        button=button.startswith('s')

        if  button:
            print("você saiu do sistema")
            break
        else:
            print("você entrou no sistema")

print("Exercise 21:")
while True:

    numberOne=input("digite o primeiro numero a ser calculado: ")
    numberTwo=input("digite o segundo numero a ser calculado: ")
    operadores=input("Digite o Operador desejado: *-+: ")

    validator_number=None
    operadores_permitidos="*-+"

    try:
        numberOneFloat= float(numberOne)
        numberTwoFloat=float(numberTwo)
        validator_number=True
    except ValueError:
       if validator_number is None:
           print("Numero invalido,digite novamente:")
           continue

    if operadores not in operadores_permitidos:
        print("Operador invalido,digite novamente:")
        continue
    elif len(operadores)<1:
        print("Digite somente um operador por vez:")
        continue

    print("Incializando Calculadora")

    if(operadores=="+"):
        calculator=numberOneFloat+numberTwoFloat
        print(f'O resultado da conta foi de %.2f'%calculator)
    elif(operadores =="-"):
        calculator=numberOneFloat-numberTwoFloat
        calculator=format(calculator,'.2f')
        print(f'O resultado da conta foi de {calculator}')
    elif(operadores=="*"):
        calculator=numberOneFloat*numberTwoFloat
        stringFormat="a={decimal:.2f}"
        calculator=stringFormat.format(decimal=calculator)
        print(f'O resultado da conta foi {calculator}')

    exit= input("Deseja sair? [s]im: ").lower().startswith('s')

    if exit:
        print("você saiu do sistema")
        break