#-*- coding:utf-8 -*-
import unittest
from should_dsl import *

from trabalho_1.bl import BancoLogico

class TestLogica(unittest.TestCase):
    def test_poupanca_adequada(self):
        bl = BancoLogico()
        bl.quantia_poupada(22000)
        bl.ganhos(25000, bl.ESTAVEL)
        bl.dependentes(3)

        bl.poupanca() |should| equal_to(bl.ADEQUADA)

    def test_renda_adequada(self):
        bl = BancoLogico()
        bl.quantia_poupada(22000)
        bl.ganhos(27000, bl.ESTAVEL)
        bl.dependentes(3)

        bl.renda() |should| equal_to(bl.ADEQUADA)

    def test_poupanca_inadequada(self):
        bl = BancoLogico()
        bl.quantia_poupada(10000)
        bl.ganhos(25000, bl.ESTAVEL)
        bl.dependentes(3)

        bl.poupanca() |should| equal_to(bl.INADEQUADA)

    def test_renda_inadequada(self):
        bl = BancoLogico()
        bl.quantia_poupada(22000)
        bl.ganhos(25000, bl.ESTAVEL)
        bl.dependentes(3)

        bl.renda() |should| equal_to(bl.INADEQUADA)

    def test_investimento(self):
        bl = BancoLogico()

        def renda(): return bl.ADEQUADA
        bl.renda = renda
        def poupanca(): return bl.ADEQUADA
        bl.poupanca = poupanca
        bl.investimento() |should| equal_to('Acoes')

        def renda(): return bl.ADEQUADA
        bl.renda = renda
        def poupanca(): return bl.INADEQUADA
        bl.poupanca = poupanca
        bl.investimento() |should| equal_to('Poupanca')

        def renda(): return bl.INADEQUADA
        bl.renda = renda
        def poupanca(): return bl.ADEQUADA
        bl.poupanca = poupanca
        bl.investimento() |should| equal_to('Ambos')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogica)
    unittest.TextTestRunner(verbosity=2).run(suite)

