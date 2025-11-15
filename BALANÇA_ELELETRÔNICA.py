# Variáveis para guardar o maior e menor peso
maior_peso = 0
menor_peso = 0
nome_maior_peso = ''
nome_menor_peso = ''

# Cores só para deixar o visual melhor no terminal
COR_VERMELHO = '\033[1;31m'
COR_VERDE = '\033[1;32m'
COR_AMARELO = '\033[1;33m'
RESET = '\033[m'

print('{:=^40}'.format(' BALANÇA ELETRÔNICA '))

# Pergunta quantas pessoas vão ser registradas
total_de_pessoas = int(input('\nQuantas pessoas iram se pesar? '))

for c in range(1, total_de_pessoas + 1):
    print('\n{:-^40}'.format(f' {c}ª PESSOA '))

    # Pega os dados básicos
    nome = str(input('Digite seu nome: ')).split()     # split só pra pegar o primeiro nome
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))

    # Cálculo do IMC
    imc = peso / (altura ** 2)

    # Verificação da classificação do IMC
    if imc < 18.5:
        cor_imc = COR_VERDE
        classificacao = f'{COR_VERDE}MAGREZA (0){RESET}'
    elif imc <= 24.9:
        cor_imc = COR_VERDE
        classificacao = f'{COR_VERDE}NORMAL (0){RESET}'
    elif imc <= 29.9:
        cor_imc = COR_AMARELO
        classificacao = f'{COR_AMARELO}SOBREPESO (I){RESET}'
    elif imc <= 39.9:
        cor_imc = COR_VERMELHO
        classificacao = f'{COR_VERMELHO}OBESIDADE (II){RESET}'
    else:
        cor_imc = COR_VERMELHO
        classificacao = f'{COR_VERMELHO}OBESIDADE GRAVE (III){RESET}'

    # Mostra o IMC e a classificação
    print('=' * 20)
    print(f'{nome[0]}, você tem o IMC {cor_imc}{imc:.2f}{RESET}, sua classificação é: {classificacao}')
    print('=' * 20)

    # Controle do maior e menor peso
    if c == 1:
        # Na primeira pessoa, só inicializa as variáveis
        maior_peso = peso
        menor_peso = peso
        nome_maior_peso = nome
        nome_menor_peso = nome
    else:
        # Verifica se este é o maior peso
        if peso > maior_peso:
            maior_peso = peso
            nome_maior_peso = nome

        # Verifica se este é o menor peso
        if peso < menor_peso:
            menor_peso = peso
            nome_menor_peso = nome

# Resultado final
print('\n' + '=' * 40)
print('{: ^40}'.format(' RESULTADO FINAL '))
print('=' * 40)

print(f'\nO ({nome_maior_peso[0]}) tem o MAIOR PESO ({maior_peso:.2f} kg)')
print(f'O ({nome_menor_peso[0]}) tem o MENOR PESO ({menor_peso:.2f} kg)')
