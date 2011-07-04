#-*- coding:utf-8 -*-
from should_dsl import should, should_not
import unittest

from trabalho_1.bl import BancoLogico

class TestRenda(unittest.TestCase):
    def test_inadequada(self):
        bl = BancoLogico()

        bl.condicao = bl.ESTAVEL
        bl.dependentes = 1
        bl.ganhos = 9999999999
        bl.renda() |should_not| equal_to(bl.INADEQUADA)
        bl.condicao = bl.INSTAVEL
        bl.renda() |should| equal_to(bl.INADEQUADA)

        bl.condicao = bl.ESTAVEL

        bl.dependentes = 1
        bl.ganhos = 18999
        bl.renda() |should| equal_to(bl.INADEQUADA)
        bl.ganhos = 19000
        bl.renda() |should_not| equal_to(bl.INADEQUADA)
        bl.ganhos = 19001
        bl.renda() |should_not| equal_to(bl.INADEQUADA)

        bl.dependentes = 2
        bl.ganhos = 22999
        bl.renda() |should| equal_to(bl.INADEQUADA)
        bl.ganhos = 23000
        bl.renda() |should_not| equal_to(bl.INADEQUADA)
        bl.ganhos = 23001
        bl.renda() |should_not| equal_to(bl.INADEQUADA)

        bl.dependentes = 3
        bl.ganhos = 26999
        bl.renda() |should| equal_to(bl.INADEQUADA)
        bl.ganhos = 27000
        bl.renda() |should_not| equal_to(bl.INADEQUADA)
        bl.ganhos = 27001
        bl.renda() |should_not| equal_to(bl.INADEQUADA)

    def test_adequada(self):
        bl = BancoLogico()

        bl.condicao = bl.INSTAVEL
        bl.dependentes = 1
        bl.ganhos = 9999999999
        bl.renda() |should_not| equal_to(bl.ADEQUADA)
        bl.condicao = bl.ESTAVEL
        bl.renda() |should| equal_to(bl.ADEQUADA)

        bl.dependentes = 1
        bl.ganhos = 18999
        bl.renda() |should_not| equal_to(bl.ADEQUADA)
        bl.ganhos = 19000
        bl.renda() |should| equal_to(bl.ADEQUADA)
        bl.ganhos = 19001
        bl.renda() |should| equal_to(bl.ADEQUADA)

        bl.dependentes = 2
        bl.ganhos = 22999
        bl.renda() |should_not| equal_to(bl.ADEQUADA)
        bl.ganhos = 23000
        bl.renda() |should| equal_to(bl.ADEQUADA)
        bl.ganhos = 23001
        bl.renda() |should| equal_to(bl.ADEQUADA)

        bl.dependentes = 3
        bl.ganhos = 26999
        bl.renda() |should_not| equal_to(bl.ADEQUADA)
        bl.ganhos = 27000
        bl.renda() |should| equal_to(bl.ADEQUADA)
        bl.ganhos = 27001
        bl.renda() |should| equal_to(bl.ADEQUADA)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRenda)
    unittest.TextTestRunner(verbosity=2).run(suite)

