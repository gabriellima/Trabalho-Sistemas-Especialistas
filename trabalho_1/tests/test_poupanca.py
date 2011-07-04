#-*- coding:utf-8 -*-
from should_dsl import should, should_not
import unittest

from trabalho_1.bl import BancoLogico

class TestPoupanca(unittest.TestCase):
    def test_inadequada(self):
        bl = BancoLogico()

        bl.dependentes = 1
        bl.quantia_poupada = 4999
        bl.poupanca() |should| equal_to(bl.INADEQUADA)
        bl.quantia_poupada = 5000
        bl.poupanca() |should_not| equal_to(bl.INADEQUADA)
        bl.quantia_poupada = 5001
        bl.poupanca() |should_not| equal_to(bl.INADEQUADA)

        bl.dependentes = 2
        bl.quantia_poupada = 9999
        bl.poupanca() |should| equal_to(bl.INADEQUADA)
        bl.quantia_poupada = 10000
        bl.poupanca() |should_not| equal_to(bl.INADEQUADA)
        bl.quantia_poupada = 10001
        bl.poupanca() |should_not| equal_to(bl.INADEQUADA)

        bl.dependentes = 3
        bl.quantia_poupada = 14999
        bl.poupanca() |should| equal_to(bl.INADEQUADA)
        bl.quantia_poupada = 15000
        bl.poupanca() |should_not| equal_to(bl.INADEQUADA)
        bl.quantia_poupada = 15001
        bl.poupanca() |should_not| equal_to(bl.INADEQUADA)

    def test_adequada(self):
        bl = BancoLogico()

        bl.dependentes = 1
        bl.quantia_poupada = 4999
        bl.poupanca() |should_not| equal_to(bl.ADEQUADA)
        bl.quantia_poupada = 5000
        bl.poupanca() |should| equal_to(bl.ADEQUADA)
        bl.quantia_poupada = 5001
        bl.poupanca() |should| equal_to(bl.ADEQUADA)

        bl.dependentes = 2
        bl.quantia_poupada = 9999
        bl.poupanca() |should_not| equal_to(bl.ADEQUADA)
        bl.quantia_poupada = 10000
        bl.poupanca() |should| equal_to(bl.ADEQUADA)
        bl.quantia_poupada = 10001
        bl.poupanca() |should| equal_to(bl.ADEQUADA)

        bl.dependentes = 3
        bl.quantia_poupada = 14999
        bl.poupanca() |should_not| equal_to(bl.ADEQUADA)
        bl.quantia_poupada = 15000
        bl.poupanca() |should| equal_to(bl.ADEQUADA)
        bl.quantia_poupada = 15001
        bl.poupanca() |should| equal_to(bl.ADEQUADA)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPoupanca)
    unittest.TextTestRunner(verbosity=2).run(suite)

