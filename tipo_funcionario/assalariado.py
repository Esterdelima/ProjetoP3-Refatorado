from modelo.funcionario_model import Funcionario
import pendulum

class Assalariado(Funcionario):

    salario = float
    valorComissao = float

    def __init__(self, nome, endereco, sindicato, id, taxaServico, salario, tipoFuncionario): #valorComissao
        super().__init__(nome, endereco, sindicato, id, taxaServico, tipoFuncionario)
        self.salario = salario
        #self.valorComissao = valorComissao


    def setSalario(self, salario):
        self.salario = salario

    # def setValorComissao(self, valorComissao):
        # self.valorComissao = valorComissao

    # def getValorComissao(self):
        # return self.valorComissao

    def getSalario(self):
        return self.salario

    # def comissao(self, salario, valorComissao):
    def salarioAssalariado(self):
        if self.sindicato > 0:
            if self.taxaServico > 0:
                return self.salario - self.sindicato - self.taxaServico
                
            else:
                return self.salario - self.sindicato
        else:
            return self.salario

    def agendar(self):
        dt = pendulum.now()
        print (dt)

        agenda = dt.end_of('month')
        if agenda.day_of_week == 5 or agenda.day_of_week == 6:
            agenda = agenda.previous(pendulum.FRIDAY)

        self.agenda = agenda
            
        

    
