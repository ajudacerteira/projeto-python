from functions import get_int, get_email
from models import ONG, Usuario, Evento

def create_ong():
    id = get_int("Digite o ID da ONG: ")
    nome = input("Digite o nome da ONG: ")
    email = get_email("Digite o email da ONG: ")
    descricao = input("Descreva a ONG: ")
    ong = ONG(id, nome, email, descricao)
    return ong 

def create_usuario():
    id 