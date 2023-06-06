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
        self.contribuicoes = {}
        
    def adicionar_contribuicoes(self, evento):
        opcao = get_int(f"\nO Usuario {self.nome} vai contribuir com este evento?\n1- Sim | 2- Não\n")
        contribuicoes = []
        if(opcao == 1):
            while True:
                item = get_string(f"Com qual insumo o {self.nome} contribuiu?\n")
                quantidade = get_int(f"Qual foi a quantidade em KG deste item?\n")
                contribuicao = Contribuicao(item, quantidade)
                contribuicoes.append(contribuicao)
                opcao = get_int(f"O {self.nome} deseja fazer alguma outra contribuição?\n1- Sim | 2- Não\n")
                if(opcao == 1):
                    continue
                elif(opcao == 2):
                    break
                else:
                    print("(Digite 1 ou 2)")
            self.contribuicoes[evento] = contribuicoes
        elif(opcao == 2):
            print(f"\nEntendido, o {self.nome} comparecerá ao envento mas sem contribuir.")
            contribuicao = Contribuicao("(nada)", "(nada)")
            contribuicoes.append(contribuicao)
            self.contribuicoes[evento] = contribuicoes
        else:
            print("(Digite 1 ou 2)")

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