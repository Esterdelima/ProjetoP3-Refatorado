from ast import Num
import pendulum
from modelo.funcionario_model import Funcionario
from tipo_funcionario.assalariado import Assalariado
from tipo_funcionario.comissario import Comissario
from tipo_funcionario.horista import Horista
from funcionalidades.crud import Crud
 


crud = Crud()

def opcoesFuncionario():
    print("\nOpções de funcionário:")
    print("""    1 - Adicionar funcionário
    2 - Remover funcionário
    3 - Alterar dados
    4 - Listar funcionários
    5 - Voltar""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
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
        novoId = int(crud.prefixo+str(crud.id))
    

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
        
        crud.criarFuncionario(funcionario)
        crud.listar()
        input('\nPressione ENTER para continuar...')

    elif escolha == 2:
        crud.listar()
        id = input('Informe o Id do funcionario que deseja remover: ')
        crud.remove(id)      

    # elif escolha == 3:
        # id = int(input("Insira o id do funcionário que fará o lançamento: "))
        # print("""Insira o tipo de lançamento:
        # 1 - Cartão de ponto
        # 2 - Comissão de venda""")
        # escolha = int(input())
        # if escolha == 1:

            # horas = int(input("Insira a quantidade de horas trabalhadas: "))
            # valorSalario = float(input("Insira o salario por horas trabalhadas: "))
            # horista = Horista(horas, valorSalario)
            # if listaFuncionario.Sindica

        # elif escolha == 2:
            # funcionarios[id].venda()
        # elif escolha == 3:
            # funcionarios[id].servico()
        # opcoes()

    elif escolha == 3:
        crud.listar()
        id = int(input("Insira o id do funcionário desejado: "))
        escolha = input("""Informe o dado que deseja alterar: 
                        1 - Nome
                        2 - Endereço
                        3 - Taxa Sindicato
                        4 - Taxa Serviço
                        5 - Tipo de Funcionario\n""")
        crud.editar(id, int(escolha))

    elif escolha == 4:
        crud.listar()
    

    elif escolha == 5:
        opcoes()
         
    else:
        print("Não entendi, vamos recomeçar o atendimento")
        opcoesFuncionario()

def opcoesFolha():
    print("\nOpções da folha:")
    print("""1 - Gerar Folha de Pagamento\n
             2 - Voltar""")
    escolha = int(input("O que deseja?\n"))
    if escolha == 1:
        crud.listar()
        valor = float
        id = int(input("Insira o id do funcionário desejado: "))
        funcionario = None
        for i in crud.listaFuncionario:
            print(' entra ', i.getId())
            if i.getId() == id:
                funcionario = i

        if not funcionario:
            print('Id não encontrado')
            return 

        print(funcionario)
        
    
        if funcionario.getTipoFuncionario() == 'Horista':
            print('entrou horista')
            valor = funcionario.cartaoPonto()
            funcionario.setValorSalario(0) 
        elif funcionario.getTipoFuncionario() == 'Assalariado':
            print('entrou assalariado')
            valor = funcionario.salarioAssalariado()
            funcionario.setSalario(0)
        else:
            print('comissario')
            valor = funcionario.comissao()
            funcionario.setTaxaComissao(0)

        funcionario.agendar()
        print('Salario: | Data de pagamento: \n', valor, funcionario.agenda)
        
    
    if escolha == 2:
        opcoesFolha()
         

def opcoes():
    print("\nMenu principal:")
    print("""1 - Espaço funcionario\n2 - Folha de Pagamento\n3 - Sair""")
    escolha = int(input("O que deseja?\n"))

    if escolha == 1:
        while(True):
            opcoesFuncionario()
    elif escolha == 2:

        opcoesFolha()
    elif escolha == 3:
        print("Obrigada por utilizar nosso sistema, volte sempre!")
        return
    else:
        print("\nNão entendi, vamos recomeçar o atendimento")
        opcoes()

print("Seja bem-vindo ao sistema Folha de Pagamento")

opcoes()