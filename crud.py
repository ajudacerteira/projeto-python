from functions import get_int, get_email, get_data, get_string, get_idade
from models import ONG, Usuario, Evento, Contribuicao

# FUNÇÕES DE CRIAÇÃO:

# Função para criar uma ONG
def create_ong():
    id = get_int("\nDigite o ID da ONG: ")
    nome = get_string("Digite o nome da ONG: ")
    email = get_email("Digite o email da ONG: ")
    descricao = get_string("Descreva a ONG: ")
    ong = ONG(id, nome, email, descricao)
    return ong 

# Função para criar um Usuario
def create_usuario():
    id = get_int("\nDigite o ID do Usuario: ")
    nome = get_string("Digite o nome do Usuario: ")
    email = get_email("Digite o email do Usuario: ")
    idade = get_idade("Digite a idade do Usuario: ")
    usuario = Usuario(id, nome, email, idade)
    return usuario

# Função para criar um Evento (lista de usuarios começa vazia)
def create_evento(ong):
    id = get_int("\nDigite o ID do Evento: ")
    nome = get_string("Digite o nome do Evento: ")
    endereco = get_string("Digite o endereco do Evento: ")
    horario = str(get_int("Digite o horario do evento: ")) + "h"
    data = get_data()
    evento = Evento(id, nome, ong, endereco, horario, data)
    return evento

def create_contribuicao(usuario):
    while True:
        opcao = get_int(f"\nO Usuario {usuario.nome} vai contribuir com este evento?\n 1- Sim | 2- Não\n")
        if(opcao == 1):
            item = get_string(f"Com qual insumo o {usuario.nome} contribuiu? ")
            quantidade = get_int(f"Qual foi a quantidade em KG deste item? ")
            contribuicao = Contribuicao(item, quantidade)
            return contribuicao
        elif(opcao == 2):
            print(f"Entendido, o {usuario.nome} comparecerá ao envento mas sem contribuir.")
            contribuicao = Contribuicao("(nada)", "(nada)")
            return contribuicao
        else:
            print("(Digite 1 ou 2)")

# FUNÇÕES PARA LISTAR INFORMAÇÕES DE UMA INTANCIA:

def listar_ong(ong):
    print(f"ONG -> {ong.id} | Nome: {ong.nome} | Email: {ong.email} | Descricao: {ong.descricao}")

def listar_usuario(usuario):
    print(f"USUARIO -> {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email} | Idade: {usuario.idade}")

def listar_contribuicao(contribuicao):
    print(f"CONTRIBUICAO -> Item: {contribuicao.item} | Quantidade em KG: {contribuicao.quantidade}")

def listar_evento(evento):
    print(f"EVENTO -> {evento.id} | Nome: {evento.nome} | ONG: {evento.ong.nome} | Endereco: {evento.endereco} | Horario: {evento.horario} | Data: {evento.data}") 
    if evento.usuarios is not None:
        for usuario in evento.usuarios:
            listar_usuario(usuario)    
            listar_contribuicao(usuario.contribuicoes[evento])

# FUNÇÕES PARA LISTAR INFOMAÇÕES DE VARIAS INSTÂNCIAS: 

def listar_ongs(ongs):
    print("")
    for ong_id, ong in ongs.items():
        listar_ong(ong)

def listar_usuarios(usuarios):
    print("")
    for usuario_id, usuario in usuarios.items():
        listar_usuario(usuario)
 

def listar_eventos(eventos):
    print("")
    for evento_id, evento in eventos.items():
        listar_evento(evento)

# FUNÇÕES QUE RETORNAM UMA INSTANCIA ESPECIFICA EM DICIONARIO

# Lista Ongs -> Pede para Digitar ID de ONG -> Retorna tal ONG
def get_ong(ongs):
    print("\nConfira todas as ONGS cadastradas: ")
    listar_ongs(ongs)
    while True:
        id = get_int("ID da ONG escolhida: ")
        for ong_id, ong in ongs.items():
            if(ong.id == id):
                return ong
            else:
                print("(Não existe uma ONG com este ID)")

# Lista Usuarios -> Pede para Digitar ID de Usuario -> Retorna tal Usuario
def get_usuario(usuarios):
    print("\nConfira todos os Usuarios cadastrados: ")
    listar_usuarios(usuarios)
    while True:
        id = get_int("ID do Usuario escolhido: ")
        for usuario_id, usuario in usuarios.items():
            if(usuario.id == id):
                return usuario
            else:
                print("(Não existe um Usuario com este ID)")

# Lista Eventos -> Pede para Digitar ID de Evento -> Retorna tal Evento
def get_evento(eventos):
    print("\n ID do Evento que deseja adicionar o Usuario: ")
    listar_eventos(eventos)
    while True:
        id = get_int("")
        for evento_id, evento in eventos.items():
            if(evento.id == id):
                return evento
            else:
                print("(Não existe um Evento com este ID)")