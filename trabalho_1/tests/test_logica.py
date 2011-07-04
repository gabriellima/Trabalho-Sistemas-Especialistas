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

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestLogica)
    unittest.TextTestRunner(verbosity=2).run(suite)

