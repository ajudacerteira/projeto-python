from functions import get_int, get_email, get_data
from models import ONG, Usuario, Evento

def create_ong():
    id = get_int("Digite o ID da ONG: ")
    nome = input("Digite o nome da ONG: ")
    email = get_email("Digite o email da ONG: ")
    descricao = input("Descreva a ONG: ")
    ong = ONG(id, nome, email, descricao)
    return ong 

def create_usuario():
    id = get_int("Digite o ID do Usuario: ")
    nome = input("Digite o nome do Usuario: ")
    email = get_email("Digite o email do Usuario: ")
    idade = get_int("Digite a idade do Usuario: ")
    usuario = Usuario(id, nome, email, idade)
    return usuario

def create_evento(ong):
    id = get_int("Digite o ID do Evento: ")
    nome = input("Digite o nome do Evento: ")
    endereco = input("Digite o endereco do Evento: ")
    horario = str(get_int("Digite o horario do evento: ")) + "h"
    data = get_data()
    evento = Evento(id, nome, ong, endereco, horario, data)
    return evento

def adicionar_usuario(usuario, evento):
    evento.usuarios.append(usuario)

def listar_ong(ong):
    print(f"ONG -> {ong.id} | Nome: {ong.nome} | Email: {ong.email} | Descricao: {ong.descricao}")

def listar_ongs(ongs):
    for ong_id, ong in ongs.items():
        listar_ong(ong)
    
def listar_usuario(usuario):
    print(f"USUARIO -> {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email} | Idade: {usuario.idade}")

def listar_usuarios(usuarios):
    for usuario_id, usuario in usuarios.items():
        listar_usuario(usuario)
    
def listar_evento(evento):
    print(f"EVENTO -> {evento.id} | Nome: {evento.nome} | ONG: {evento.ong} | Endereco: {evento.endereco} | Horario: {evento.horario} | Data: {evento.data}") 

def listar_eventos(eventos):
    for evento_id, evento in eventos.items():
        listar_evento(evento)

def get_ong(ongs):
    print("Digite o ID da ONG criadora do Evento: ")
    listar_ongs(ongs)
    id = get_int("")
    for ong in ongs.values():
        if(ong.id == id):
            return ong

def get_usuario(usuarios):
    print("Digite o ID do Usuario que deseja adicionar: ")
    listar_usuarios(usuarios)
    id = get_int()
    for usuario in usuarios.items():
        if(usuario.id == id):
            return usuario

def get_evento(eventos):
    print("Digite o ID do Evento que deseja adicionar o Usuario: ")
    listar_eventos()
    id = get_int()
    for evento in eventos.items():
        if(evento.id == id):
            return evento