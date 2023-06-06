from functions import get_int, get_string

# Classe ONG 
class ONG:
    def __init__(self, id, nome, email, descricao):
        self.id = id
        self.nome = nome
        self.email = email
        self.descricao = descricao
    
# Classe Usuario
class Usuario: 
    def __init__(self, id, nome, email, idade):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade
        
class Contribuicao:
    def __init__(self, item, quantidade):
        self.item = item
        self.quantidade = quantidade

# Classe Evento -> Tem uma ONG e uma lista de Usuarios como Atributo
class Evento:
    def __init__(self, id, nome, ong, endereco, horario, data):
        self.id = id
        self.nome = nome
        self.ong = ong
        self.endereco = endereco
        self.horario = horario
        self.data = data
        self.usuarios = []
        self.contribuicoes = {}

    def adicionar_contribuicoes(self, usuario):
        contribuicoes = []
        while True:
            item = get_string(f"\nCom qual insumo o {usuario.nome} contribuiu?\n")
            quantidade = get_int(f"\nQual foi a quantidade em KG deste item?\n")
            contribuicao = Contribuicao(item, quantidade)
            contribuicoes.append(contribuicao)
            opcao = get_int(f"\nO {usuario.nome} deseja fazer alguma outra contribuição?\n1- Sim | (Outro Numero)- Não\n")
            if(opcao == 1):
                continue
            break
        self.contribuicoes[usuario] = contribuicoes
       