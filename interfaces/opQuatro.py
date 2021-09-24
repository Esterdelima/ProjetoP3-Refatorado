from interfaces.comando import Command


class ListarFuncionario(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.opQuatro() 