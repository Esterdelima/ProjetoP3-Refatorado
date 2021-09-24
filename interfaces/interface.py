from tipo_funcionario.comissario import Comissario
from tipo_funcionario.horista import Horista
from tipo_funcionario.assalariado import Assalariado
from funcionalidades.crud import Crud


class Interface():
    def __init__(self):
        pass

    def opUm():
        nome = input("Insira o nome do funcionario a ser adicionado:\n")
        endereco = input("Insira o endereço do funcionario a ser adicionado:\n")
        print("""Faz parte de sindicato:
        1 - Sim
        2 - Não""")
        escolha = int(input())
        while escolha > 2:
            escolha = int(input("Não entendi, escolha novamente: "))
        if escolha == 1:
            taxaSindicato = float(input('Informe a taxa de Sindicato:\n'))
            escolha = int(input("""Paga alguma Taxa de Serviço?
                                    1 - Sim
                                    2 - Não\n"""))
            if escolha == 1:
                taxaServico = int(input('Informe a taxa de Serviço: \n'))
            else:
                taxaServico = 0
        else:
            taxaSindicato = 0
            taxaServico = 0
        novoId = int(Crud.id)
        tipoFuncionario = int(input("""Informe sua função:
                                1- Horista
                                2 - Assalariado
                                3 - Comissário\n"""))
        if tipoFuncionario == 1:
            valorSalario = float(input('Informe seu salário por hora: \n'))
            horas = float(input('Informe a hora trabalhada:\n'))
            funcionario = Horista(nome,endereco, taxaSindicato, novoId, taxaServico, horas, valorSalario, 'Horista')
        elif tipoFuncionario == 2:
            salario = float(input('Informe seu salário: \n'))
            funcionario = Assalariado(nome,endereco, taxaSindicato, novoId, taxaServico, salario, 'Assalariado')
        elif tipoFuncionario == 3:
            taxaComissao = float(input('Informe a sua comissão: \n'))
            funcionario = Comissario(nome,endereco,taxaSindicato, novoId, taxaServico, taxaComissao, 'Comissario')
                
        Crud.criarFuncionario(funcionario)
        Crud.listar()
        input('\nPressione ENTER para continuar...')

    def opDois():
        Crud.listar()
        id = input('Informe o Id do funcionario que deseja remover: ')
        Crud.remove(id)      

    def opTres():
        Crud.listar()
        id = int(input("Insira o id do funcionário desejado: "))
        escolha = input("""Informe o dado que deseja alterar: 
                    1 - Nome
                    2 - Endereço
                    3 - Taxa Sindicato
                    4 - Taxa Serviço
                    5 - Tipo de Funcionario\n""")
        Crud.editar(id, int(escolha))

    def opQuatro():
        Crud.listar()


