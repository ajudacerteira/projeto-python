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
        ong = get_ong
        create_evento(ong)
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")
