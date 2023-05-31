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
        if len(ongs) == 0:
            print("\n(Você precisa criar pelo menos 1 ONG antes)")
            continue
        ong = get_ong(ongs)
        evento = create_evento(ong)
        eventos[evento.id] = evento
    elif opcao == 4: # Adicionar Usuario em Evento
        if len(eventos) == 0 or len(usuarios) == 0:
            print("\n(Você precisa criar pelo menos 1 evento e 1 usuario antes)")
            continue
        evento = get_evento(eventos)
        usuario = get_usuario(usuarios)
        contribuicao = create_contribuicao(usuario)
        if contribuicao is not None:
            usuario.adicionar_contribuicao(evento, contribuicao)
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
