class Contato:
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email
class Agenda:
    def __init__(self):
        self.contatos = []
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    def remover_contato(self, contato):
        self.contatos.remove(contato)
    def listar_contatos(self):
        for contato in self.contatos:
            print("Nome:", contato.nome)
            print("Endereço:", contato.endereco)
            print("E-mail:", contato.email)
agenda = Agenda()
contato1 = Contato("João", "Rua A, 123", "joao@example.com")
contato2 = Contato("Maria", "Rua B, 456", "maria@example.com")
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.listar_contatos()
agenda.remover_contato(contato1)
agenda.listar_contatos()

#O comando class cria um objeto nesse caso cria o objeto contato que possui os atributos nome endereço e email, e criou o objeto agenda que possui vários contatos armazenados.
#O código definiu sozinho os objetos mas na maioria das vezes, vem em forma de prompt para que o usuário cadastre as informações dentro do objeto.
#O código definiu cada um dos atributos aos objetos e após isso os exibiu, porém nesse código após exibir 1 vez, o código apaga contato1
#por isso apenas o contato2 é exibido na tela após ser listado novamente.