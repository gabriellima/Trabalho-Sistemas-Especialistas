#-*- coding:utf-8 -*-
class BancoLogico:
    ADEQUADA = True
    INADEQUADA = False
    ESTAVEL = True
    INSTAVEL = False

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

    def renda(self):
        if self.condicao and self.ganhos >= 15000+(4000*self.dependentes):
            return self.ADEQUADA
        else:
            return self.INADEQUADA

