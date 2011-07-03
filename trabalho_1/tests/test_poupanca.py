#-*- coding:utf-8 -*-
from should_dsl import should, should_not
import unittest

from trabalho_1.bl import BancoLogico

class TestPoupanca(unittest.TestCase):
    def test_poupanca_inadequada(self):
        bl = BancoLogico()

        dependentes = 1
        quantia_poupada = 4999
        bl.poupanca(dependentes, quantia_poupada) |should| \
                                                         equal_to(bl.INADEQUADA)
        quantia_poupada = 5000
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                         equal_to(bl.INADEQUADA)
        quantia_poupada = 5001
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                         equal_to(bl.INADEQUADA)

        dependentes = 2
        quantia_poupada = 9999
        bl.poupanca(dependentes, quantia_poupada) |should| \
                                                         equal_to(bl.INADEQUADA)
        quantia_poupada = 10000
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                         equal_to(bl.INADEQUADA)
        quantia_poupada = 10001
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                         equal_to(bl.INADEQUADA)

        dependentes = 3
        quantia_poupada = 14999
        bl.poupanca(dependentes, quantia_poupada) |should| \
                                                   equal_to(bl.INADEQUADA)
        quantia_poupada = 15000
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                   equal_to(bl.INADEQUADA)
        quantia_poupada = 15001
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                   equal_to(bl.INADEQUADA)

    def test_poupanca_adequada(self):
        bl = BancoLogico()

        dependentes = 1
        quantia_poupada = 4999
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                   equal_to(bl.ADEQUADA)
        quantia_poupada = 5000
        bl.poupanca(dependentes, quantia_poupada) |should| equal_to(bl.ADEQUADA)
        quantia_poupada = 5001
        bl.poupanca(dependentes, quantia_poupada) |should| equal_to(bl.ADEQUADA)

        dependentes = 2
        quantia_poupada = 9999
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                   equal_to(bl.ADEQUADA)
        quantia_poupada = 10000
        bl.poupanca(dependentes, quantia_poupada) |should| equal_to(bl.ADEQUADA)
        quantia_poupada = 10001
        bl.poupanca(dependentes, quantia_poupada) |should| equal_to(bl.ADEQUADA)

        dependentes = 3
        quantia_poupada = 14999
        bl.poupanca(dependentes, quantia_poupada) |should_not| \
                                                   equal_to(bl.ADEQUADA)
        quantia_poupada = 15000
        bl.poupanca(dependentes, quantia_poupada) |should| equal_to(bl.ADEQUADA)
        quantia_poupada = 15001
        bl.poupanca(dependentes, quantia_poupada) |should| equal_to(bl.ADEQUADA)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPoupanca)
    unittest.TextTestRunner(verbosity=2).run(suite)

