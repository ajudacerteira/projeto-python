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

def get_int(numero):
    while True:
        try:
            value = input(numero)
            value = int(value)
            return value
        except ValueError:
            print("Digite um número inteiro")