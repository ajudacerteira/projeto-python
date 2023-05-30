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