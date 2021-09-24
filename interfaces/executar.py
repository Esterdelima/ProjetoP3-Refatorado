class Executar():

    def __init__(self):
        self.slot = None

    def setComando(self, command):
        self.slot = command

    def Escolha(self):
        return self.slot.execute()