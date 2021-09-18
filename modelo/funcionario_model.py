
class Funcionario():
    nome = ''
    endereco = ''
    id = int
    sindicato = float
    valorSalario = float
    taxaServico = float
    tipoFuncionario = str
    

    def __init__(self, nome, endereco, sindicato, id, taxaServico, tipoFuncionario):
        self.nome = nome
        self.endereco = endereco
        self.sindicato = sindicato
        self.id = id
        self.taxaServico = taxaServico
        self.tipoFuncionario = tipoFuncionario
        self.agenda = self.agendar()


    def toString(self):
        return 'Nome: ' + self.getNome() + ' | Endereço: ' + self.getEndereco() + ' | Taxa Sindicato: ' + str(self.getSindicato())  + ' | Taxa Serviço: ' + str(self.getTaxaServico()) + ' | Funcionario: ' + self.getTipoFuncionario() + ' | Id: ' + str(self.getId())

    def setNome(self, nome):
        self.nome = nome

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setSindicato(self, sindicato):
        self.endereco = sindicato

    def setValorSalario(self, valorSalario):
        self.valorSalario = valorSalario

    def setTaxaServico(self, taxaServico):
        self.taxaServico = taxaServico

    def setTipoFuncionario(self,tipoFuncionario):
        self.tipoFuncionario = tipoFuncionario
    
    def getTipoFuncionario(self):
        return self.tipoFuncionario

    def getTaxaServico(self):
        return self.taxaServico

    def getValorSalario(self):
        return self.valorSalario

    def getNome(self):
        return self.nome

    def getEndereco(self):
        return self.endereco

    def getSindicato(self):
        return self.sindicato

    def getId(self):
        return self.id
