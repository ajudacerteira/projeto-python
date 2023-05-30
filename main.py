from crud import *
from functions import *

ongs = {}
usuarios = {}
eventos = {}

while True:
    opcao = mostrar_menu()
    if opcao == 1:
        ong = create_ong()
        ongs[ong.id] = ong
    elif opcao == 2:
        usuario = create_usuario()
        usuarios[usuario.id] = usuario
    elif opcao == 3:
        ong = get_ong(ongs)
        evento = create_evento(ong)
        eventos[evento.id] = evento
    elif opcao == 4:
        evento = get_evento(eventos)
        usuario = get_usuario(usuarios)
        adicionar_usuario(usuario, evento)
    elif opcao == 5:
        listar_ongs(ongs)
    elif opcao == 6:
        listar_usuarios(usuarios)
    elif opcao == 7:
        listar_eventos(eventos)  
    elif opcao == 0:
        break         
    else:
        print("Opção inválida!")
