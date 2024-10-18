import os

# Lista global para armazenar valores de IMC
valueImc = []

def usr_data():
    """
    Coleta dados do usuário: nome, altura e peso.

    Retorna:
        None
    """
    print('='*100)
    print('Calculadora IMC')
    print('='*100)
    print("Seu nome deve conter apenas letras e espaço\nMáximo 30 caracteres")
    usr_name = input('Informe seu nome: ')
    valid = valid_date(usr_name, 'name')
    
    print("Informe sua altura em centímetros\nExemplo 170")
    usr_height = input('Informe sua Altura: ')
    valid = valid_date(usr_height, 'height')
    
    print("Informe seu peso em quilos\nExemplo 75")
    usr_weight = input('Informe seu Peso: ')
    valid = valid_date(usr_weight, 'weight')

def valid_date(input, name):
    """
    Valida a entrada do usuário com base no tipo de dado (nome, altura, peso).

    Parâmetros:
        input (str): Entrada do usuário.
        name (str): Tipo de dado ('name', 'height', 'weight').

    Retorna:
        None
    """
    global valueImc
    msg_error = True  # Inicializa como verdadeiro para indicar ausência de erros

    # Valida o nome
    if name == 'name':
        # Verifica se o nome contém apenas letras e espaços
        if not input.replace(' ', '').isalpha(): 
            msg_error = 'Informe um nome válido. * Apenas letras e espaços'
        if len(input) > 30:  # Verifica se o nome tem menos de 30 caracteres
            msg_error = 'Informe um nome menor'

    # Valida a altura e peso
    elif (name == 'height' or name == 'weight') and not input.isdecimal():
        msg_error = 'Informe um valor válido. * Apenas números'

    # Se houver erro, imprime a mensagem e reseta valueImc
    if msg_error != True:
        print(msg_error)
        valueImc = []
        restApp()
    else:
        valueImc.append(input)  # Adiciona a entrada válida à lista valueImc
        clear_screen() # Chama função para limpar o terminal
        if len(valueImc) == 3:  # Se a lista tiver 3 elementos, calcula o IMC
            calc_imc(valueImc)

def restApp():
    """
    Pergunta ao usuário se deseja preencher os dados novamente ou sair do aplicativo.

    Retorna:
        None
    """
    msg = input('Preencher novamente? [s/n]')
    if msg.lower() == 's':
        global valueImc
        valueImc = []  # Reseta a lista valueImc
        clear_screen() # Chama função para limpar o terminal
        usr_data()  # Chama a função para coletar dados do usuário novamente
    else:
        clear_screen() # Chama função para limpar o terminal
        exit()  # Sai do aplicativo

def clear_screen():
    """
    Limpa a tela do terminal com base no sistema operacional.

    Retorna:
        None
    """
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix (Linux/Mac)
        os.system('clear')

def calc_imc(usr_Value):
    """
    Calcula o Índice de Massa Corporal (IMC) com base na altura e peso do usuário.

    Parâmetros:
        usr_Value (list): Lista contendo nome, altura e peso do usuário.

    Retorna:
        None
    """
    usr_height = float(usr_Value[1]) / 100  # Altura do usuário em FLOAT transformada em metros
    usr_weight = int(usr_Value[2])  # Peso do usuário em INT
    calc = usr_weight / usr_height ** 2  # Calcula o IMC
    calc = f"{calc:.2f}"  # Formata para duas casas decimais
    calc = float(calc)

    # Classifica o IMC
    if calc <= 18.5:
        classified = 'Magro'
    elif 18.5 <= calc <= 24.9:
        classified = 'Normal'
    elif 25 <= calc <= 29.9:
        classified = 'Sobrepeso'
    elif 30 <= calc <= 39.9:
        classified = 'Obeso'
    else:
        classified = 'Obesidade Grave'

    print(f"{usr_Value[0]}! Seu cálculo foi concluído")
    print(f"Seu peso é de {usr_Value[2]}\nSeu IMC é de {calc}")
    print(f"Sua classificação é {classified.upper()}")
    print('\n')
    restApp()

usr_data() # Inicia a coleta de dados do usuário