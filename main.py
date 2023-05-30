from crud import *
from functions import *

ongs = {}
usuarios = {}
eventos = {}

while True:
    opcao = mostrar_menu()
    if opcao == 1: # Criar ONG
        ong = create_ong()
        ongs[ong.id] = ong
    elif opcao == 2: # Criar Usuario
        usuario = create_usuario()
        usuarios[usuario.id] = usuario
    elif opcao == 3: # Criar Evento
        ong = get_ong(ongs)
        evento = create_evento(ong)
        eventos[evento.id] = evento
    elif opcao == 4: # Adicionar Usuario em Evento
        evento = get_evento(eventos)
        usuario = get_usuario(usuarios)
        evento.usuarios.append(usuario)
    elif opcao == 5: # Listar ONGS
        listar_ongs(ongs)
    elif opcao == 6: # Listar Usuarios
        listar_usuarios(usuarios)
    elif opcao == 7: # Listar Eventos
        listar_eventos(eventos)  
    elif opcao == 0:
        break # Sair      
    else:
        print("Opção inválida!")
