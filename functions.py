# Mostra as Opções do Menu e valida opção inexistente
def mostrar_menu():
    print("\nSelecione uma Opção")
    print("1 - Cadastrar nova ONG | 2- Cadastrar novo Usuario | 3- Cadastrar novo Evento")
    print("4 - Adicionar Usuario em Evento")
    print("5 - Listar ONGs | 6 - Listar Usuarios | 7 - Listar Eventos")
    print("0 - Sair")
    try:
        option = int(input())
        return option
    except ValueError:
        print("(Digite um opção válida)")

# Validar email Inputado pelo Usuario
def get_email(mensagem):
    while True:
        email = input(mensagem)
        if(email.__contains__("@") and email.__contains__(".com")):
            return email         
        print("(Email deve conter @ e .com)")

# Validar numero Inputado pelo Usuario
def get_int(mensagem):
    while True:
        try:
            value = input(mensagem)
            value = int(value)
            return value
        except ValueError:
            print("(Digite um número inteiro)")

# Validar idade Inputada pelo Usuario
def get_idade(mensagem):
    while True:
        idade = get_int(mensagem)
        if(idade < 12 or idade > 110):
            print("(Digite uma idade valida)")
            continue
        return idade

# Validar data Inputada pelo Usuario
def get_data():
    dia = 0
    mes = 0
    while True:
        dia = get_int("Digite o Dia do Evento: ")
        if(dia < 1 or dia > 31):
            print("(Digite um dia valida)")
            continue
        break
    while True: 
        mes = get_int("Digite o Mês do Evento: ")
        if(mes < 1 or mes > 12):
            print ("(Digite um mês valido)")
            continue
        break
    
    return str(str(dia) + "/" + str(mes))