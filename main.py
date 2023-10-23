from function import graus
from function import fah

while True:

    print('\n\t\t -- CONVERSÃO GRAUS/FAHRENHEIT')

    print('1. Transformar Graus em Fahrenheit')
    print('2. Transformar Fahrenheit em Graus')
    print('3. Sair')

    op = int(input('Opção: '))
    print('\n')

    if op == 1:
        valor = float(input('Digite a temperatura em graus celsius: '))
        print(graus(valor))

    elif op == 2:
        valor = float(input('Digite a temperatura em fahrenheit: '))
        print(fah(valor))

    elif op == 3:
        print('Tchauuu :) ')
        break

    else:
        print('Opção não identificada')
