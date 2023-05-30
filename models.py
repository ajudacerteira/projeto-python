class ONG:
    def __init__(self, id, nome, email, descricao):
        self.id = id
        self.nome = nome
        self.email = email
        self.descricao = descricao
    

class Usuario: 
    def __init__(self, id, nome, email, idade):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade

class Evento:
    def __init__(self, id, ong, nome, endereco, horario, data, descricao):
        self.id = id
        self.nome = nome
        self.ong = ong
        self.endereco = endereco
        self.horario = horario
        self.data = data
        self.descricao = descricao
        self.usuarios = []