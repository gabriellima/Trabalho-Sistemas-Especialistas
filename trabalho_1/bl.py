#-*- coding:utf-8 -*-
class BancoLogico:
    ADEQUADA = True
    INADEQUADA = False

    def poupanca(self, numero_de_dependentes, quantia_poupada):
        if quantia_poupada >= 5000*numero_de_dependentes:
            return self.ADEQUADA
        else:
            return self.INADEQUADA

    def renda(self, numero_de_dependentes, ganhos):
        if ganhos >= 15000+(4000*numero_de_dependentes):
            return self.ADEQUADA
        else:
            return self.INADEQUADA

