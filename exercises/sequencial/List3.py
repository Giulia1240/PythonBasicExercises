"""11-Faça um exemplo com interpolação utilizando o nome Luiz e o preço de um playtation
limitando seu valor em duas casas decimais.

12-Faça um programa que dobre qualquer número que você digitar.

13-CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

14-Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

15-Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

16-Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

"""
print('exercicio11')
name="Luiz"
price=1000.200
var=' %s ,the playstation is $ %.2f' %(name,price)

print(var)

print("===================================================================================================")
print('exercicio12')
number_str= input('Vou dobrar o numero que você digitar: ')

try:
    numberFloat= float(number_str)
    numberDouble=numberFloat * 2
    formatNumber=format(numberDouble,'.2f')

    print(f'O dobro de {number_str} é o numero {formatNumber}')
except:
    print("Valor invalido")
print("===================================================================================================")
print('exercicio13')

velocidade = input("Digite a Velocidade: ")  # velocidade atual do carro
local_carro = input('Digite a distância que o carro se encontra: ')  # local em que o carro está na estrada

formatingVelocidade=int(velocidade)
formattingLocal=int(local_carro)

RADAR_1 = 61  # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

carroNaoPassouNoPerimetroDoRadar = formattingLocal < (LOCAL_1 - RADAR_RANGE) and formatingVelocidade > RADAR_1 or formatingVelocidade <= RADAR_1
carroNoPerimetroDoRadar = formattingLocal <= LOCAL_1 and formatingVelocidade > RADAR_1 or formatingVelocidade <= RADAR_1
carroComVelocidadeMenorEPassouPeloPerimtroDoRadar = formattingLocal >= (LOCAL_1 + RADAR_RANGE) and formatingVelocidade <= RADAR_1
carroComAltaVelocidadeQuePassouPeloPerimetroDoRadar = formattingLocal >= (LOCAL_1 + RADAR_RANGE) and formatingVelocidade >= RADAR_1
if carroNaoPassouNoPerimetroDoRadar:
    print(f'Carro localizado a {formattingLocal} m de distância não foi multado por conta da velocidade em {formatingVelocidade}')
elif carroNoPerimetroDoRadar:
    print(f'Carro localizado a {formattingLocal} m de distância foi multado por conta da velocidade em {formatingVelocidade}')
elif carroComVelocidadeMenorEPassouPeloPerimtroDoRadar:
    print(f'Carro localizado a {formattingLocal} m de distância não foi multado, pois sua velocidade é {formatingVelocidade}')
elif carroComAltaVelocidadeQuePassouPeloPerimetroDoRadar:
    print(f'Carro localizado a {formattingLocal}  m de distância foi multado por conta da velocidade em {formatingVelocidade}')
else:
    print("Não identificado")
print("===================================================================================================")
print("Exercicio 14:")
while True:
    try:
        number=int(input('Digite um numero inteiro:'))
        par= number%2==0
        impar=number%2!=0
        if par:
            print(f'O número {number} é par')
        elif impar:
            print(f'O número {number} é impar')
        break
    except ValueError:
        print("Você não Digitou um numero válido")
print("===================================================================================================")
print("Exercicio 15")
while True:
    try:
        hours=int(input("Digite que horas são em numeros inteiros: "))
        bomDia= hours >=0 and hours <= 11
        boaTarde=hours >= 12 and hours <= 17
        boaNoite=hours >= 18 and  hours <=23

        if bomDia:
            print("Bom dia")
        elif boaTarde:
            print("Boa tarde")
        elif boaNoite:
            print("Boa noite")
        break
    except ValueError:
        print("Valor inválido")
print("===================================================================================================")
print("Exercicio 16:")

while True:
    try:
        userName= input("Digite seu nome:")
        sizeName=len(userName)

        smallName=sizeName<=4
        mediumName=sizeName>=5 and sizeName <=6
        largeName=sizeName>6

        if smallName:
            print("O seu nome de usuario é pequeno")
        elif mediumName:
            print("Seu nome é normal")
        elif largeName:
            print("Seu nome é muito grande")

        break

    except ValueError:
        print("Nome inválido")