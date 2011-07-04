#-*- coding:utf-8 -*-
class BancoLogico:
    #TODO: converter comentários em documentação de funções
    #TODO: converter comentários para português

    ADEQUADA = True
    INADEQUADA = False
    ESTAVEL = True
    INSTAVEL = False

    #functions used to set params
    def quantia_poupada(self, valor):
        self.quantia_poupada = valor

    def ganhos(self, valor, condicao):
        self.ganhos = valor
        self.condicao = condicao

    def dependentes(self, quantidade):
        self.dependentes = quantidade

    def poupanca(self):
        if self.quantia_poupada >= 5000*self.dependentes:
            return self.ADEQUADA
        else:
            return self.INADEQUADA
    #function aliases (without logic), needing to have different hashes
    def poupanca_adequada(self):
        return self.poupanca() == True
    def poupanca_inadequada(self):
        return self.poupanca() == False

    def renda(self):
        if self.condicao and self.ganhos >= 15000+(4000*self.dependentes):
            return self.ADEQUADA
        else:
            return self.INADEQUADA
    #function aliases (without logic), needing to have different hashes
    def renda_adequada(self):
        return self.renda() == True
    def renda_inadequada(self):
        return self.renda() == False

    #function that give result
    def investimento(self):
        if not self.poupanca():
            return 'Poupanca'
        elif self.renda():
            return 'Acoes'
        else:
            return 'Ambos'
    #function aliases (without logic), needing to have different hashes
    def investimento_poupanca(self):
        return self.investimento() == 'Poupanca'
    def investimento_acoes(self):
        return self.investimento() == 'Acoes'
    def investimento_ambos(self):
        return self.investimento() == 'Ambos'

    def investimento_seguro(self):
        return True

    def __call__(self):
        return  True

