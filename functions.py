def mostrar_menu():
    print("Selecione uma das opções")
    print("1 - Cadastrar ONG")
    print("2 - Cadastrar Usuario")
    print("3 - Cadastrar Evento")
    print("0 - Sair")

    try:
        option = int(input())
        return option
    except ValueError:
        print("Digite um opção válida")

def get_email(mensagem):
    while True:
        email = input(mensagem)
        if(email.__contains__("@") and email.__contains__(".com")):
            return email

         

def get_int(mensagem):
    while True:
        try:
            value = input(mensagem)
            value = int(value)
            return value
        except ValueError:
            print("Digite um número inteiro")

def get_idade(mensagem):
    while True:
        idade = get_int()
        if(idade < 12 and idade > 110):
            print("Digite uma idade valida")
            continue
        return idade

def get_data(mensagem):
    dia = 0
    mes = 0
    while True:
        dia = get_int()
        if(dia < 1 and dia > 31):
            print("Digite uma idade valida")
            continue
        break
    while True: 
        mes = get_int()
        if(mes < 1 and mes > 12):
            print ("Digite um dia valido")
            continue
        break
    return str(dia + "/" + mes)
        
        