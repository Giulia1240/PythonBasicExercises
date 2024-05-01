"""
1.Você deve imprimir a mensagem "Hello World!" e em seguida o final de linha, conforme o exemplo abaixo.
=======================================================================================================================================================
2.Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X.
Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado
e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

=======================================================================================================================================================
3.A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

=======================================================================================================================================================
4.Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir,
calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11).
Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço
em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça
de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
=======================================================================================================================================================

"""
print("Exercise 01:\n")
print("Hello World")

print("===================================================================================================")
print("Exercise 02:\n")
a=input("Insert the value for A attribute:\n")
b=input("Insert the value for B attribute:\n")
x=int(a)+int(b)
print(f'The X value is:{x}')

print("===================================================================================================")
print("Exercise 03: \n")
"""area = π . raio2"""
pi=3.1415
raio= input("Insert the raio value: ")
convertRaio=int(raio)

area=pi*pow(convertRaio,2)
formatingArea=format(area,'.2f')
print(f'A area do circulo é:{formatingArea} \n')

print("===================================================================================================")
print("Exercise 04: \n")
gradeOne=input("Insert the value for first grade:\n")
gradeSecond=input("Insert the value for second grade:\n")

gradeA=float(gradeOne)
gradeB=float(gradeSecond)
pesoOne=3.5
pesoTwo=7.5

media= (gradeA*pesoOne)+(gradeB*pesoTwo)/2

formating="x={decimal:.2f}"
mediaFormating=formating.format(decimal=media)

print(f'MEDIA: {mediaFormating}')




