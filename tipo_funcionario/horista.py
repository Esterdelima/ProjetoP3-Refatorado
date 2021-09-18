from modelo.funcionario_model import Funcionario
import pendulum

class Horista(Funcionario):

    valorSalario = float
    

    def __init__(self, nome, endereco, sindicato, id, taxaServico, horas, valorSalario, tipoFuncionario):
        super().__init__(nome, endereco, sindicato, id, taxaServico, tipoFuncionario)
        self.horas = horas
        self.valorSalario = valorSalario

    
    def setHoras(self, horas):
        self.horas = horas

    def setValorSalario(self, valorSalario):
        self.valorSalario = valorSalario

    def getValorSalario(self):
        return self.valorSalario

    def getHoras(self):
        return int(self.horas)


    def cartaoPonto(self):
        extra = float
        if self.horas > 8:
            if self.sindicato > 0:  
                if self.taxaServico > 0: 
                        extra = self.valorSalario * 1.5 * (self.horas-8)
                        return (8*self.valorSalario)+extra - self.sindicato - self.taxaServico
            else:
                taxaServico = 0
                sindicato = 0
                extra = self.valorSalario * 1.5 * (self.horas-8)
                return (8*self.valorSalario)+extra - self.sindicato
        else:
            return self.valorSalario*self.horas
    
    def agendar(self):
        dt = pendulum.now()
        print (dt)
        agenda = dt.next(pendulum.FRIDAY)
        self.agenda = agenda
