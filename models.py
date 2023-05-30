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
    def __init__(self, id, nome, endereco, horario, descricao, produtos, usuarios):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.horario = horario
        self.descricao = descricao
        self.produtos = produtos
        self.usuarios = usuarios