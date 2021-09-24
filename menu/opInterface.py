from main import opcoesFuncionario, opcoesFolha


class Menu():
    def __init__(self):
        pass

    def opFuncionario(self):
        opcoesFuncionario()

    def opFolha(self):
        opcoesFolha()

    def opEncerra(self):
        print("Obrigada por utilizar nosso sistema, volte sempre!")
        exit()