


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
