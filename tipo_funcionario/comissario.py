from modelo.funcionario_model import Funcionario
import pendulum

class Comissario(Funcionario):

    taxaComissao = float


    def __init__(self, nome, endereco, sindicato, id, taxaServico, taxaComissao, tipoFuncionario):
        super().__init__(nome, endereco, sindicato, id, taxaServico, tipoFuncionario)
        self.taxaComissao = taxaComissao


    def setTaxaComissao(self, taxaComissao):
        self.taxaComissao = taxaComissao

    def getTaxaComissao(self):
        return self.taxaComissao

    def comissao(self):
        novoSalario = float
        if self.sindicato > 0:
            if self.taxaServico > 0:
                novoSalario = self.taxaComissao - self.sindicato - self.taxaServico
                return novoSalario
            else:
                novoSalario = self.taxaComissao - self.sindicato
            return novoSalario
        else:
            return self.taxaComissao


    def agendar(self):
        dt = pendulum.now()
        print (dt)
        agenda = dt.next(pendulum.FRIDAY)
        agenda = agenda.add(weeks=2)
        self.agenda = agenda
    