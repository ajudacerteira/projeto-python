from functions import get_int, get_email, get_data, get_string, get_idade
from models import ONG, Usuario, Evento

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

# FUNÇÕES PARA LISTAR INFORMAÇÕES DE UMA INTANCIA:

def listar_ong(ong):
    print(f"ONG -> {ong.id} | Nome: {ong.nome} | Email: {ong.email} | Descricao: {ong.descricao}")

def listar_usuario(usuario):
    print(f"USUARIO -> {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email} | Idade: {usuario.idade}")

def listar_evento(evento):
    print(f"EVENTO -> {evento.id} | Nome: {evento.nome} | ONG: {evento.ong.nome} | Endereco: {evento.endereco} | Horario: {evento.horario} | Data: {evento.data}") 
    for usuario in evento.usuarios:
        listar_usuario(usuario)    

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
    print("\n Confira todas as ONGS cadastradas: ")
    listar_ongs(ongs)
    id = get_int("Digite o ID da ONG escolhida: ")
    for ong_id, ong in ongs.items():
        if(ong.id == id):
            return ong

# Lista Usuarios -> Pede para Digitar ID de Usuario -> Retorna tal Usuario
def get_usuario(usuarios):
    print("\nConfira todos os Usuarios cadastrados: ")
    listar_usuarios(usuarios)
    id = get_int("Digite o ID do Usuario escolhido: ")
    for usuario_id, usuario in usuarios.items():
        if(usuario.id == id):
            return usuario

# Lista Eventos -> Pede para Digitar ID de Evento -> Retorna tal Evento
def get_evento(eventos):
    print("\nDigite o ID do Evento que deseja adicionar o Usuario: ")
    listar_eventos(eventos)
    id = get_int("")
    for evento_id, evento in eventos.items():
        if(evento.id == id):
            return evento