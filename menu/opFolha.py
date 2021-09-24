from interfaces.comando import Command


class OpFolha(Command):

    def __init__(self, interface):
        self.interface = interface

    def execute(self):
        return self.interface.encerraMenu() 