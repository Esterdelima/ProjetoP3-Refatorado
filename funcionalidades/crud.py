from modelo.funcionario_model import Funcionario
import random
listaFuncionario = []

class Crud:

    id = 0
    
    def criarFuncionario(self):
        self.id = random.randint(1, 10000) 
        listaFuncionario.append(self)


    def listar():
        print("Lista de Funcionarios: \n")
        for f in listaFuncionario: 
            print(f.toString())

    def remove(id):
        indexes = [index for index in range(len(listaFuncionario)) if listaFuncionario[index].getId() == int(id)]
        if len(indexes) == 0:
            print('Id não encontrado')
            return 
        listaFuncionario.pop(indexes[0])

    def editar(id, edita):
        indexes = [index for index in range(len(listaFuncionario)) if listaFuncionario[index].getId() == int(id)]
        if len(indexes) == 0:
            print('Id não encontrado')
            return 
        if edita == 1:
            valor = input('Insira o novo dado: ')
            listaFuncionario[indexes[0]].setNome(valor)
        elif edita == 2:
            valor = input('Insira o novo dado: ')
            listaFuncionario[indexes[0]].setEndereco(valor)
        elif edita == 3:
            valor = input('Insira o novo dado: ')
            listaFuncionario[indexes[0]].setSindicato(valor)
        elif edita == 4:
            valor = input('Insira o novo dado: ')
            listaFuncionario[indexes[0]].setTaxaServico(valor)
        elif edita == 5:
            valor = input('Insira o novo dado: ')
            listaFuncionario[indexes[0]].setTipoFuncionario(valor)
    
    
    
    
    
    
    

                                