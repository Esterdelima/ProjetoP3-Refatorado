from modelo.funcionario_model import Funcionario

class Crud:

    listaFuncionario = []
    prefixo = '13'
    id = 0

    
    def criarFuncionario(self, funcionario):
        self.id += 1
        self.listaFuncionario.append(funcionario)


    def listar(self):
        print("Lista de Funcionarios: \n")
        for f in self.listaFuncionario: 
            print(f.toString())

    def remove(self, id):
        indexes = [index for index in range(len(self.listaFuncionario)) if self.listaFuncionario[index].getId() == int(id)]
        if len(indexes) == 0:
            print('Id não encontrado')
            return 
        self.listaFuncionario.pop(indexes[0])

    def editar(self, id, edita):
        indexes = [index for index in range(len(self.listaFuncionario)) if self.listaFuncionario[index].getId() == int(id)]
        if len(indexes) == 0:
            print('Id não encontrado')
            return 
        if edita == 1:
            valor = input('Insira o novo dado: ')
            self.listaFuncionario[indexes[0]].setNome(valor)
        elif edita == 2:
            valor = input('Insira o novo dado: ')
            self.listaFuncionario[indexes[0]].setEndereco(valor)
        elif edita == 3:
            valor = input('Insira o novo dado: ')
            self.listaFuncionario[indexes[0]].setSindicato(valor)
        elif edita == 4:
            valor = input('Insira o novo dado: ')
            self.listaFuncionario[indexes[0]].setTaxaServico(valor)
        elif edita == 5:
            valor = input('Insira o novo dado: ')
            self.listaFuncionario[indexes[0]].setTipoFuncionario(valor)
    
    
    
    
    
    
    

                                